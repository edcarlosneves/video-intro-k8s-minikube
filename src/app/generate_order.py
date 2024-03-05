import json
import os
import random
import uuid
from datetime import datetime, timedelta

from fastapi import FastAPI


def generate_order_value():
    return random.randint(10000, 100000) / 100


def generate_order_id():
    return str(uuid.uuid4())


def create_order():
    order_id = generate_order_id()
    order_value = generate_order_value()
    return order_id, order_value


def get_order_delivery(order_date):
    return order_date + timedelta(days=7)


app = FastAPI()


@app.post("/new_order")
def new_order():
    order_date = datetime.now()
    order_delivery = get_order_delivery(order_date)
    order_id, order_value = create_order()
    return {
        "order_id": order_id,
        "order_value": order_value,
        "order_date": order_date,
        "order_delivery": order_delivery,
    }
