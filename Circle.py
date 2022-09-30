# IMPORTS
from Shape import *


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
        return (self.radios ** 2) * 3.14

    def Perimeter_Calculation(self):
        """
        calculates the perimeter of self(circle)
        :return: the area of self
        """
        return (self.radios * 2) * 3.14

    def Get_Radios(self):
        """
        :return: the radios of self(circle)
        """
        return self.radios
