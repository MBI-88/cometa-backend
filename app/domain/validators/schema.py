from typing import List
from pydantic import BaseModel

class OrderItemSchema(BaseModel):
    name: str
    quantity: int

class RoundSchema(BaseModel):
    created: str
    items: List[OrderItemSchema]

class OrderSchema(BaseModel):
    created: str
    paid: bool
    subtotal: float
    taxes: float
    discounts: float
    items: List[OrderItemSchema]
    rounds: List[RoundSchema]

class ItemSchema(BaseModel):
    name: str
    price_per_unit: float
    total: float