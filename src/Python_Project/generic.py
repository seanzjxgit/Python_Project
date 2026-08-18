from typing import List,TypeVar,Generic

class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

AnimalType = TypeVar('AnimalType',bound=Animal,covariant=True)

class Store(Generic[AnimalType]):
    def __init__(self,stock: List[AnimalType]) -> None:
        self.stock = stock

    def buy(self) -> AnimalType:
        return self.stock.pop()

wang = Store[Dog]([Dog(),Dog()])
print(wang.buy())