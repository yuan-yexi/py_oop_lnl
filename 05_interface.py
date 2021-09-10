# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to implement interfaces
# An interface is a kind of promise

from abc import ABC, abstractmethod


# TODO: this is a interface that indicates a class knows this function
class JSONify(ABC):
    @abstractmethod
    def to_json(self):
        pass


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self) -> float:
        return 3.14 * (self.radius ** 2)

    def to_json(self):
        return f"{{\"circle\": {str(self.calcArea())}}}"


c = Circle(10)
print(c.calcArea())
print(c.to_json())
