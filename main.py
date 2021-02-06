from fastapi import FastAPI, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi_login import LoginManager
from starlette.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
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

app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)


@manager.user_loader
def load_user(username: str):  # could also be an asynchronous function
    user = users_table.search('username', username)
    if user:
        return user[0]['fields']
    else:
        return None


@app.post('/auth/token')
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
    return {'access_token': access_token, 'token_type': 'bearer'}


@app.get("/products")
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


@app.get("/products/{pid}")
async def get_product(pid: str):
    products_raw = products_table.get_all(fields=['id', 'name', 'images', 'price', 'category', 'short_description', 'description', 'weight', 'dimensions'])
    products = []
    for product in products_raw:
        p = product['fields']
        if p['id'] == pid:
            p['images'] = [i['url'] for i in p['images']]
            products.append(p)
    return JSONResponse(content=jsonable_encoder(products[0]))


