# IMPORTS
from Rectangle import *


class Square(Rectangle):
    def __init__(self, colour, area, perimeter, edge):
        """
        The Square object
        :param colour: colour of Square
        :param area: area of Square
        :param perimeter: perimeter of Square
        :param edge: edge(the side) of Square
        """
        super().__init__(colour, area, perimeter, edge, edge)
        self.edge = edge

    def Get_Edge(self):
        """
        :return: the edge of the Square
        """
        return self.edge

    def Area_Calculation(self):
        """
        Calculates the area of the Square
        :return: the area of the Square
        """
        return self.edge ** 2

    def Perimeter_Calculation(self):
        """
        Calculates the perimeter of the Square
        :return: the perimeter of the Square
        """
        return self.edge * 4


if __name__ == '__main__':
    square = Square("Black", 25, 20, 5)
    assert square.Get_Colour() == "Black"
    assert square.Get_Area() == 25
    assert square.Get_Perimeter() == 20
    assert square.Get_Edge() == 5
