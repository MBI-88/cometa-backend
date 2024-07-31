from app.domain.repositories.repo import InMemoryRepository, Order 



def get_order() -> Order:
    return InMemoryRepository.get_order()
