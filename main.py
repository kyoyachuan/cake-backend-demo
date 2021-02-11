import os
import base64
from datetime import datetime, timedelta
from typing import List, Optional

import aiofiles
from fastapi import FastAPI, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.staticfiles import StaticFiles
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi_login import LoginManager
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from airtable import Airtable

from setting import Setting as setting


if not os.path.exists('images'):
    os.makedirs('images')

app = FastAPI()
app.mount("/images", StaticFiles(directory="images"), name="images")

manager = LoginManager(setting.JWT_SECRET_KEY, tokenUrl='/auth/token')

products_table = Airtable(
        setting.AIRTABLE_BASE_KEY,
        'products',
        setting.AIRTABLE_API_KEY,
)
cards_table = Airtable(
        setting.AIRTABLE_BASE_KEY,
        'cards',
        setting.AIRTABLE_API_KEY,
)
users_table = Airtable(
        setting.AIRTABLE_BASE_KEY,
        'users',
        setting.AIRTABLE_API_KEY,
)
orders_table = Airtable(
        setting.AIRTABLE_BASE_KEY,
        'orders',
        setting.AIRTABLE_API_KEY,
)
carts_table = Airtable(
        setting.AIRTABLE_BASE_KEY,
        'carts',
        setting.AIRTABLE_API_KEY,
)

app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)


class RegisterForm(BaseModel):
    username: str
    email: str
    password: str


class ProductToCarts(BaseModel):
    id: int
    quantity: Optional[int] = 1


class Card(BaseModel):
    name: str
    front: str
    back: str


class CartsUpdateQuantity(BaseModel):
    id: int
    quantity: int


class Carts(BaseModel):
    id: int


class CartsToOrders(BaseModel):
    ids: List[int]


@manager.user_loader
def load_user(username: str):  # could also be an asynchronous function
    user = users_table.search('username', username)
    if user:
        user[0]['fields']['record_id'] = user[0]['id']
        return user[0]['fields']
    else:
        return None


@app.post('/auth/token', tags=['users'])
async def login(data: OAuth2PasswordRequestForm = Depends()):
    username = data.username
    password = data.password

    user = load_user(username)  # we are using the same function to retrieve the user
    if not user:
        raise InvalidCredentialsException  # you can also use your own HTTPException
    elif password != user['password']:
        raise InvalidCredentialsException

    access_token = manager.create_access_token(
        data=dict(sub=username), expires_delta=timedelta(hours=24)
    )
    return {
        'access_token': access_token,
        'token_type': 'Bearer',
        'username': username,
        'num_carts': sum(user['total_carts']) if 'total_carts' in user.keys() else 0,
        'num_orders': len(user['orders']) if 'orders' in user.keys() else 0,
        'num_cards': len(user['cards']) if 'cards' in user.keys() else 0,
    }


@app.post('/signup', tags=['users'])
async def signup(data: RegisterForm):
    username = data.username
    password = data.password
    email = data.email

    if len(users_table.search('username', username)) != 0:
        raise HTTPException(status_code=404, detail="Username used!")
    elif len(users_table.search('email', email)) != 0:
        raise HTTPException(status_code=405, detail="Email used!")
    else:
        users_table.insert({
            'username': username,
            'password': password,
            'email': email
        })
        return {'status': 'success!'}


@app.get("/products", tags=['products'])
async def get_products(category: str = None):
    products_raw = products_table.get_all(fields=['id', 'name', 'main_image', 'price', 'category'])
    products = []
    for product in products_raw:
        p = product['fields']
        if not category:
            p['image'] = p['main_image'][0]['url']
            p.pop('main_image')
            products.append(p)
        elif p['category'] == category:
            p['image'] = p['main_image'][0]['url']
            p.pop('main_image')
            products.append(p)
    return JSONResponse(content=jsonable_encoder(products))


@app.get("/products/{pid}", tags=['products'])
async def get_product(pid: int):
    product = products_table.search(
            'id', pid,
            fields=['id', 'name', 'images', 'price', 'category', 'short_description', 'description', 'weight', 'dimensions']
    )[0]['fields']
    product['images'] = [i['url'] for i in product['images']]
    return JSONResponse(content=jsonable_encoder(product))


@app.get("/orders", tags=['orders'])
async def get_orders(user = Depends(manager)):
    uid = user['id']
    orders = orders_table.search('user', uid)
    orders = [order['fields'] for order in orders]
    return orders


@app.post("/make_orders", tags=['orders'])
async def make_orders(data: CartsToOrders, user = Depends(manager)):
    urid = user['record_id']
    cids = data.ids

    products_id_list = []
    product_quantity = []
    cards_id_list = []
    amount = 0
    for cid in cids:
        cart = carts_table.search('id', cid)[0]['fields']
        if 'product' in cart.keys():
            products_id_list.append(cart['product'][0])
            product_quantity.append(str(cart['quantity']))
            amount = amount + (cart['quantity'] * cart['product_price'][0])
        elif 'card' in cart.keys():
            cards_id_list.append(cart['card'][0])

    order = {
        'user': [urid],
        'products': products_id_list,
        'product_quantity': ','.join(product_quantity),
        'amount': amount,
    }
    if cards_id_list:
        order['cards'] = cards_id_list

    result = orders_table.insert(order)

    for cid in cids:
        carts_table.delete_by_field('id', cid)

    return result


@app.get("/carts", tags=['carts'])
async def get_carts(user = Depends(manager)):
    uid = user['id']
    carts = carts_table.search('user', uid)
    carts = [cart['fields'] for cart in carts]
    for cart in carts:
        if 'product_main_image' in cart.keys():
            cart['product_main_image'] = cart['product_main_image'][0]['url']
        elif 'card_front' in cart.keys():
            cart['card_front'] = cart['card_front'][0]['url']
    return carts


@app.post("/add_product_to_carts", tags=['carts'])
async def add_product_to_carts(data: ProductToCarts, user = Depends(manager)):
    urid = user['record_id']
    pid = data.id
    quantity = data.quantity

    carts = carts_table.search('user', user['id'])
    product_in_carts = None
    if carts:
        product_in_carts = [cart for cart in carts if 'product_id' in cart['fields'].keys() and cart['fields']['product_id'][0] == pid]

    if product_in_carts:
        cart_record_id = product_in_carts[0]['id']
        quantity += product_in_carts[0]['fields']['quantity']
        result = carts_table.update(cart_record_id, {'quantity': quantity})

    else:
        product = products_table.search('id', pid)[0]
        prid = product['id']

        data_insert = {
            'user': [urid],
            'product': [prid],
            'quantity': quantity,
            'type': 'product',
        }

        result = carts_table.insert(data_insert)

    return result['fields']


@app.post("/add_card_to_carts", tags=['carts'])
async def add_card_to_carts(data: Card, user = Depends(manager)):
    urid = user['record_id']
    file_name = datetime.now().strftime("%Y%m%d%H%M%S") + '.png'
    front_imgstr = data.front[data.front.find(",")+1:]
    back_imgstr = data.back[data.back.find(",")+1:]
    front_imgdata = base64.b64decode(front_imgstr)
    back_imgdata = base64.b64decode(back_imgstr)

    async with aiofiles.open('images/front_' + file_name, mode='wb') as f:
        await f.write(front_imgdata)
    async with aiofiles.open('images/back_' + file_name, mode='wb') as f:
        await f.write(back_imgdata)

    card_data = {
        'user': [urid],
        'name': data.name,
        'front': [{'url': setting.HOSTNAME + f'images/front_{file_name}'}],
        'back': [{'url': setting.HOSTNAME + f'images/back_{file_name}'}],
        'price': 0,
    }

    card_result = cards_table.insert(card_data)

    cart_data = {
        'user': [urid],
        'card': [card_result['id']],
        'quantity': 1,
        'type': 'card',
    }

    cart_result = carts_table.insert(cart_data)
    return cart_result


@app.patch("/update_carts", tags=['carts'])
async def update_carts(data: CartsUpdateQuantity, user = Depends(manager)):
    urid = user['record_id']
    cid = data.id
    quantity = data.quantity

    record = carts_table.search('id', cid)[0]

    result = carts_table.update(record['id'], {'quantity': quantity})
    return result['fields']


@app.delete("/delete_carts", tags=['carts'])
async def delete_carts(data: Carts, user = Depends(manager)):
    urid = user['record_id']
    cid = data.id

    record = carts_table.search('id', cid)[0]

    carts_table.delete(record['id'])
    return {'message': 'success!'}


