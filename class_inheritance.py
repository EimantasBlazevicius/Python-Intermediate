from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def corner_count(self):
        pass

    @abstractmethod
    def sides_count(self):
        pass


class Sqaure(Shape):
    def __init__(self, number):
        self.number = number

    def corner_count(self):
        return self.number

    def sides_count(self):
        return self.number


shape = Sqaure(5)
print(shape.corner_count())
