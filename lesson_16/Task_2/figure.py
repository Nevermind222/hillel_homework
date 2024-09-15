from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        ...
    @abstractmethod
    def calculate_square(self):
        ...

