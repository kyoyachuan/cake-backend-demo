from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from airtable import Airtable

from setting import Setting as setting


app = FastAPI()
products_table = Airtable(
        setting.AIRTABLE_BASE_KEY,
        'products',
        setting.AIRTABLE_API_KEY,
)

app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)


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
        print(p)
        if p['id'] == pid:
            p['images'] = [i['url'] for i in p['images']]
            products.append(p)
    return JSONResponse(content=jsonable_encoder(products[0]))


