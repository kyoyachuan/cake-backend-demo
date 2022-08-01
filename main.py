import os
import base64
from datetime import datetime, timedelta

import aiofiles
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.staticfiles import StaticFiles
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi_login import LoginManager
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import cloudinary
import cloudinary.uploader
import cloudinary.api

from setting import Setting as setting
from database import SessionLocal, engine
import models
import schemas
import crud


models.Base.metadata.create_all(bind=engine)
config = cloudinary.config(secure=True)

if not os.path.exists('images'):
    os.makedirs('images')

app = FastAPI()
app.mount("/images", StaticFiles(directory="images"), name="images")

manager = LoginManager(setting.JWT_SECRET_KEY, tokenUrl='/auth/token')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@manager.user_loader
def load_user(username: str, db: Session = SessionLocal()):  # could also be an asynchronous function
    return crud.get_user(db, username=username)


@app.post('/auth/token', tags=['users'])
async def login(data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    username = data.username
    password = data.password

    user = load_user(username)  # we are using the same function to retrieve the user
    if not user:
        raise HTTPException(status_code=406, detail="User was not exists!")
    elif password != user.password:
        raise HTTPException(status_code=408, detail="Password was wrong!")

    access_token = manager.create_access_token(
        data=dict(sub=username), expires=timedelta(hours=24)
    )
    return {
        'access_token': access_token,
        'token_type': 'Bearer',
        'username': username,
        'num_carts': len(crud.get_carts(db, user.id)),
        'num_orders': len(crud.get_orders(db, user.id)),
        'num_cards': len(crud.get_cards(db, user.id)),
    }


@app.post('/signup', tags=['users'])
async def signup(data: schemas.RegisterForm, db: Session = Depends(get_db)):
    if crud.get_user(db, username=data.username):
        raise HTTPException(status_code=404, detail="Username used!")
    elif crud.get_user(db, email=data.email):
        raise HTTPException(status_code=405, detail="Email used!")
    else:
        crud.create_user(db, data)
        return {'status': 'success!'}


@app.get("/products", tags=['products'])
async def get_products(category: str = None, db: Session = Depends(get_db)):
    return crud.get_products(db, category=category)


@app.get("/products/{pid}", tags=['products'])
async def get_product(pid: int, db: Session = Depends(get_db)):
    return crud.get_product(db, pid)


@app.get("/card-font", tags=['cards'])
async def get_card_font(db: Session = Depends(get_db)):
    return crud.get_card_font(db)


@app.get("/card-decorations", tags=['cards'])
async def get_card_decorations(db: Session = Depends(get_db)):
    return crud.get_card_decorations(db)


@app.get("/orders", tags=['orders'])
async def get_orders(user=Depends(manager), db: Session = Depends(get_db)):
    return crud.get_orders(db, user.id)


@app.post("/make_orders", tags=['orders'])
async def make_orders(data: schemas.CartsToOrders, user=Depends(manager), db: Session = Depends(get_db)):
    timestamp = datetime.now()
    product_id_list = []
    product_quantity = []
    card_id_list = []
    amount = 0
    for cid in data.ids:
        cart = crud.get_cart(db, cid)
        print(cart)
        if cart.product_id:
            product_id_list.append(cart.product_id)
            product_quantity.append(cart.quantity)
            amount += cart.product.price * cart.quantity
        elif cart.card_id:
            card_id_list.append(cart.card_id)
            amount += cart.card.price
    oid = crud.create_order(db, user.id, amount, timestamp)

    for pid, quantity in zip(product_id_list, product_quantity):
        crud.create_order_product(db, oid, pid, quantity, timestamp)
    for cid in card_id_list:
        crud.create_order_card(db, oid, cid, timestamp)

    for cid in data.ids:
        crud.delete_cart(db, cid)

    return {'status': 'success!'}


@app.get("/carts", tags=['carts'])
async def get_carts(user=Depends(manager), db: Session = Depends(get_db)):
    return crud.get_carts(db, user.id)


@app.post("/add_product_to_carts", tags=['carts'])
async def add_product_to_carts(data: schemas.ProductToCarts, user=Depends(manager), db: Session = Depends(get_db)):
    timestamp = datetime.now()
    carts = crud.get_carts(db, user.id)
    product_in_carts = None
    for cart in carts:
        if cart.product_id == data.id:
            product_in_carts = cart
            break

    if product_in_carts:
        crud.update_cart(db, data)
    else:
        crud.create_cart_with_product(db, data, user.id, timestamp)
    return {'status': 'success!'}


@app.post("/add_card_to_carts", tags=['carts'])
async def add_card_to_carts(data: schemas.Card, user=Depends(manager), db: Session = Depends(get_db)):
    timestamp = datetime.now()
    file_name = timestamp.strftime("%Y%m%d%H%M%S") + '.png'
    front_imgstr = data.front[data.front.find(",")+1:]
    back_imgstr = data.back[data.back.find(",")+1:]
    front_imgdata = base64.b64decode(front_imgstr)
    back_imgdata = base64.b64decode(back_imgstr)

    async with aiofiles.open('images/front_' + file_name, mode='wb') as f:
        await f.write(front_imgdata)
    async with aiofiles.open('images/back_' + file_name, mode='wb') as f:
        await f.write(back_imgdata)

    front_url = cloudinary.uploader.upload('images/front_' + file_name)['url']
    back_url = cloudinary.uploader.upload('images/back_' + file_name)['url']

    card = schemas.Card(
        front=front_url,
        back=back_url,
        name=data.name,
    )

    card_result = crud.create_card(db, card, user.id)

    cart_result = crud.create_cart_with_card(db, card_result.id, user.id, timestamp)
    return cart_result


@app.patch("/update_carts", tags=['carts'])
async def update_carts(data: schemas.CartsUpdateQuantity, user=Depends(manager), db: Session = Depends(get_db)):
    return crud.update_cart(db, data)


@app.delete("/delete_carts", tags=['carts'])
async def delete_carts(data: schemas.Carts, user=Depends(manager), db: Session = Depends(get_db)):
    crud.delete_cart(db, data.id)
    return {'status': 'success!'}
