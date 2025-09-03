import base64
from typing import List
from urllib.request import Request

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import Response, JSONResponse

app = FastAPI()


class Characteristic(BaseModel):
    max_speed: int
    max_fuel_capacity : int


class Car(BaseModel):
    identifier : str
    brand : str
    model : str
    characteristics : Characteristic

stored_car  = []


@app.get("/ping")
async def ping():
    return Response(content="pong", status_code=200, media_type="application/json")


@app.post("/cars")
def create_car(car_payload: List[Car]):
    stored_car.append(car_payload)
    serialized_car = car_serialized()
    return Response(content=serialized_car, status_code=200, media_type="text/plain")

def car_serialized():
    serialized_car = []
    for c in stored_car:
        serialized_car.append(c.model_dump())
    return serialized_car

@app.get("/cars")
def list_cars():
    return stored_car

@app.get("/cars/{identifier}")
def get_car(identifier: int):
    for i, car in enumerate(stored_car):
        if car.identifier == identifier:
            return car[i]
    return Response(content="Car not found or doesn't exist", status_code=404, media_type="text/plain")
