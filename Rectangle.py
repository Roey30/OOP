# IMPORTS
from Shape import *


class Rectangle(Shape):
    def __init__(self, colour, area, perimeter, edge1, edge2):
        """
        The Rectangle object
        :param colour: colour of Rectangle
        :param area: area of Rectangle
        :param perimeter: perimeter of Rectangle
        :param edge1: edge1(one side) of Rectangle
        :param edge2: edge2(other side) of Rectangle
        """
        super().__init__(colour, area, perimeter)
        self.edge1 = edge1
        self.edge2 = edge2

    def Get_Edge1(self):
        """
        :return: the first edge of self
        """
        return self.edge1

    def Get_Edge2(self):
        """
        :return: the second edge of self
        """
        return self.edge2

    def Area_Calculation(self):
        """
        calculates the area of self (rectangle)
        :return: the area of self
        """
        return self.edge1 * self.edge2

    def Perimeter_Calculation(self):
        """
        :return: the area of self
        """
        return (self.edge1 * 2) + (self.edge2 * 2)

    def Combine_Shapes(self, new_shape):
        """
        :param new_shape: different shape from the main (Square or Rectangle)
        :return: combines between shapes (Square + Square,Square + Rectangle, Rectangle + Rectangle)
        """
        print(f'shape: edge1: {new_shape.Get_Edge1()} edge2: {new_shape.Get_Edge2()}'
              f'rectangle: edge1: {self.edge1} edge2: {self.edge2} ')
        if self.edge1 == self.edge2:
            if new_shape.Get_Edge1() == new_shape.Get_Edge2():
                return f'Square + Square = {self.Get_Area() + new_shape.Get_Area()}'
            else:
                if self.edge1 == new_shape.Get_Edge1():
                    return f'Square + rectangle = {(self.edge2 + new_shape.Get_Edge2()) * self.edge1}'
                elif self.edge2 == new_shape.Get_edge2():
                    return f'Square + rectangle = {(self.edge1 + new_shape.Get_Edge1()) * self.edge2}'
        else:
            if new_shape.Get_Edge1() == new_shape.Get_Edge2():
                if self.edge1 == new_shape.Get_Edge1():
                    return f'Rectangle + square = {(self.edge2 + new_shape.Get_Edge2()) * self.edge1}'
                elif self.edge2 == new_shape.Get_Edge2():
                    return f'Rectangle + square = {(self.edge1 + new_shape.Get_Edge1()) * self.edge2}'
            else:
                if self.edge1 == new_shape.Get_Edge1():
                    return f'Rectangle + rectangle = {(self.edge2 + new_shape.Get_Edge2()) * self.edge1}'
                elif self.edge1 == new_shape.Get_Edge2():
                    return f'Rectangle + rectangle = {(self.edge1 + new_shape.Get_Edge1()) * self.edge1}'
                elif self.edge2 == new_shape.Get_Edge1():
                    return f'Rectangle + rectangle = {(self.edge1 + new_shape.Get_Edge1()) * self.edge2}'
                elif self.edge2 == new_shape.Get_Edge2():
                    return f'Rectangle + rectangle = {(self.edge1 + new_shape.Get_Edge1()) * self.edge2}'
        return f'Areas not combinable'


if __name__ == '__main__':
    rectangle = Rectangle("Black", 40, 26, 5, 8)
    assert rectangle.Get_Colour() == "Black"
    assert rectangle.Get_Area() == 40
    assert rectangle.Get_Perimeter() == 26
    assert rectangle.Get_Edge1() == 5
    assert rectangle.Get_Edge2() == 8
