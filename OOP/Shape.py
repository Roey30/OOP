class Shape:
    def __init__(self, colour, area, perimeter):
        """
        The Shape object
        :param colour: colour of Rectangle
        :param area: area of Rectangle
        :param perimeter: perimeter of Rectangle
        """
        self.colour = colour
        self.area = area
        self.perimeter = perimeter

    def Set_Colour(self, new_colour):
        """
        Sets a new colour for the object
        :param new_colour: new colour from the main
        """
        self.colour = new_colour

    def Set_Area(self, new_area):
        """
        Sets a new area for the object
        :param new_area: new area from the main
        """
        self.area = new_area

    def Set_Perimeter(self, new_perimeter):
        """
        Sets a new perimeter for the object
        :param new_perimeter: new perimeter from the main
        """
        self.perimeter = new_perimeter

    def Get_Colour(self):
        """
        :return: the colour of the shape
        """
        return self.colour

    def Get_Area(self):
        """
        :return: the area of the shape
        """
        return self.area

    def Get_Perimeter(self):
        """
        :return: the perimeter of the shape
        """
        return self.perimeter


if __name__ == '__main__':
    shape = Shape("Blue", 30, 45)
    assert shape.Get_Colour() == "Blue"
    assert shape.Get_Area() == 30
    assert shape.Get_Perimeter() == 45
