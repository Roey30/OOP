# IMPORTS
from Shape import *
import math


class Circle(Shape):
    def __init__(self, colour, area, perimeter, radios):
        """
        The Circle object
        :param colour: colour of circle
        :param area: area of circle
        :param perimeter: perimeter of circle
        :param radios: radios of circle
        """
        super().__init__(colour, area, perimeter)
        self.radios = radios

    def Area_Calculation(self):
        """
        calculates the area of self(circle)
        :return: the area of self
        """
        return (self.radios ** 2) * math.pi

    def Perimeter_Calculation(self):
        """
        calculates the perimeter of self(circle)
        :return: the area of self
        """
        return (self.radios * 2) * math.pi

    def Get_Radios(self):
        """
        :return: the radios of self(circle)
        """
        return self.radios


if __name__ == '__main__':
    circle = Circle("Yellow", 78.539, 31.415, 5)
    assert circle.Get_Colour() == "Yellow"
    assert circle.Get_Area() == 78.539
    assert circle.Get_Perimeter() == 31.415
    assert circle.Get_Radios() == 5
