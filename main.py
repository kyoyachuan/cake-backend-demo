from fastapi import FastAPI

app = FastAPI()


@app.get("/items")
def read_item():
    return {"item_id": 100}


