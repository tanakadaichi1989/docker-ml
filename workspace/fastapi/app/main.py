# 参考資料
# https://qiita.com/yota_dev/items/ab8dea7f71c8a130d5bf
# https://qiita.com/amuyikam/items/ef3f8e8e25c557f68f6a
# https://fastapi.tiangolo.com/ja/

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

@app.post("/items")
def update_item(item: Item):
    print("［POST］" + " " + item.name + " " + str(item.price))
    print(sampleMethod())
    return {"item_name": item.name, "twice price": item.price * 2}


def sampleMethod():
    return "sampleMethod was executed."
