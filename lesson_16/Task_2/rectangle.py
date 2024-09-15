from typing import override

from figure import Figure


class Rectangle(Figure):

    __rectangle_a: int
    __rectangle_b: int

    def __init__(self, rectangle_a: int, rectangle_b: int):
        self.__rectangle_b = rectangle_b
        self.__rectangle_a = rectangle_a

    @override
    def calculate_perimeter(self):
        return (self.__rectangle_a * 2) + (self.__rectangle_b * 2)

    @override
    def calculate_square(self):
        return self.__rectangle_a * self.__rectangle_b

