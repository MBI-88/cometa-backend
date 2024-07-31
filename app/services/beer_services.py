from typing import List
from app.domain.repositories.repo import InMemoryRepository, Beer, Order, OrderItem


def get_beers() -> List[Beer]:
    return InMemoryRepository.get_beers()

def get_beer_status(name: str) -> str:
    return InMemoryRepository.get_beer_status(name)