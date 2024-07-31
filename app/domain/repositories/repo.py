from typing import List, Dict
from datetime import datetime
from app.domain.models.models import *



stock: Dict[str, any] = {
    "last_updated": "2024-09-10 12:00:00",
    "beers": [
        {"name": "Corona", "price": 115, "quantity": 2},
        {"name": "Quilmes", "price": 120, "quantity": 0},
        {"name": "Club Colombia", "price": 110, "quantity": 3},
    ]
}

current_order: Dict[str, any] = {
    "created": "2024-09-10 12:00:00",
    "paid": False,
    "subtotal": 0,
    "taxes": 0,
    "discounts": 0,
    "items": [
        {
            "name": "Quilmes",
            "price_per_unit": 0,
            "total": 0
        }
    ],
    "rounds": [
         {
            "created":  "2024-09-10 12:00:30",
            "items": [
                {
                    "name": "Corona",
                    "quantity": 2
                },
                {
                    "name": "Club Colombia",
                    "quantity": 1
                }
            ]
        },
        {
            "created":  "2024-09-10 12:20:31",
            "items": [
                {
                    "name": "Club Colombia",
                    "quantity": 1
                },
                {
                    "name": "Quilmes",
                    "price": 2
                }
            ]
        },
        {
            "created":  "2024-09-10 12:43:21",
            "items": [
                {
                    "name": "Quilmes",
                    "quantity": 3
                }
            ]
        }
    ]
}

class InMemoryRepository:
    @staticmethod
    def get_beers() -> List[Beer]:
        return stock["beers"]

    @staticmethod
    def get_beer_status(name: str) -> str:
        beer = next((b for b in stock["beers"] if b["name"].lower() == name.lower()), None)
        if beer is None:
            raise ValueError("Beer not found")
        return "Available" if beer["quantity"] > 0 else "Out of stock"

    @staticmethod
    def get_order() -> Order:
        return current_order
