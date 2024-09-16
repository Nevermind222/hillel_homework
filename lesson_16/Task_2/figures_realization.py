from figure import Figure
from triangle import Triangle
from rectangle import Rectangle
from square import Square

square: Square = Square(10)

rectangle: Rectangle = Rectangle(10, 5)

triangle: Triangle = Triangle(5, 6, 9, 3)

figure_list: list[Figure] = [square, rectangle, triangle]

list_tuple_perimeter_and_square: list[tuple[int, object]] = [(figure.calculate_perimeter(), figure.calculate_square())
                                                             for figure in figure_list]

for item in list_tuple_perimeter_and_square:
    print(item[0], item[1])