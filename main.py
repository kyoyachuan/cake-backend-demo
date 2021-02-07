from typing import Optional

from fastapi import FastAPI, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi_login import LoginManager
from starlette.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from airtable import Airtable

from setting import Setting as setting


app = FastAPI()
manager = LoginManager(setting.JWT_SECRET_KEY, tokenUrl='/auth/token')


products_table = Airtable(
        setting.AIRTABLE_BASE_KEY,
        'products',
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


@manager.user_loader
def load_user(username: str):  # could also be an asynchronous function
    user = users_table.search('username', username)
    if user:
        user[0]['fields']['record_id'] = user[0]['id']
        return user[0]['fields']
    else:
        return None


@app.post('/auth/token', tags=['login'])
async def login(data: OAuth2PasswordRequestForm = Depends()):
    username = data.username
    password = data.password

    user = load_user(username)  # we are using the same function to retrieve the user
    if not user:
        raise InvalidCredentialsException  # you can also use your own HTTPException
    elif password != user['password']:
        raise InvalidCredentialsException

    access_token = manager.create_access_token(
        data=dict(sub=username)
    )
    return {
        'access_token': access_token,
        'token_type': 'Bearer',
        'num_carts': len(user['carts']),
        'num_orders': len(user['orders']),
        'num_cards': len(user['cards']),
    }


@app.post('/signup', tags=['signup'])
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
async def get_product(pid: str):
    products_raw = products_table.get_all(fields=['id', 'name', 'images', 'price', 'category', 'short_description', 'description', 'weight', 'dimensions'])
    products = []
    for product in products_raw:
        p = product['fields']
        if p['id'] == pid:
            p['images'] = [i['url'] for i in p['images']]
            products.append(p)
    return JSONResponse(content=jsonable_encoder(products[0]))


@app.get("/orders", tags=['orders'])
async def get_orders(user = Depends(manager)):
    uid = user['id']
    orders = orders_table.search('user', uid)
    orders = [order['fields'] for order in orders]
    return orders


@app.get("/carts", tags=['carts'])
async def get_carts(user = Depends(manager)):
    uid = user['id']
    carts = carts_table.search('user_id', uid)
    carts = [cart['fields'] for cart in carts]
    return carts







