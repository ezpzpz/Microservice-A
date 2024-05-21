from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Item(BaseModel):
    type: str
    distance: str


@app.post("/")
async def create_item(item: Item):
    distance_dict = item.dict()

    if distance_dict["type"] == "miles":

        distance = distance_dict["distance"]

        converted = float(distance) * 1.60934
        converted = str(converted)
    elif distance_dict["type"] == "kilometers":
        distance = distance_dict["distance"]

        converted = float(distance) * 0.621371
        converted = str(converted)
    else:
        converted = "type incorrect"

    return converted


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
