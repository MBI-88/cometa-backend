from pydantic import BaseModel
from typing import List

class Beer(BaseModel):
    name: str
    price: float
    quantity: int

class OrderItem(BaseModel):
    name: str
    price_per_unit: int

class Round(BaseModel):
    created: str
    items: List[OrderItem]

class Order(BaseModel):
    created: str
    paid: bool
    subtotal: float
    taxes: float
    discounts: float
    items: List[OrderItem]
    rounds: List[Round]

class Item(BaseModel):
    name: str
    price_per_unit: float
    total: float