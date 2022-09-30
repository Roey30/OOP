# IMPORTS
from Circle import *
from Square import *
import random

LIST_COLOUR = ['BLUE', 'YELLOW', 'RED', 'GREEN', 'BLACK', 'BROWN', 'WHITE', 'PURPLE', 'PINK', 'ORANGE']
LIBRARY_COLOUR = {'BLUE': 0, 'YELLOW': 0, 'RED': 0, 'GREEN': 0, 'BLACK': 0, 'BROWN': 0, 'WHITE': 0,
                  'PURPLE': 0, 'PINK': 0, 'ORANGE': 0}


class Container(Shape):
    """
    class of object shape

    """
    def __init__(self):
        super().__init__(colour=None, area=None, perimeter= None)
        self.list_shapes = []
        self.colour = ''

    def Generate(self, number_shapes, min_edge, max_edge):
        """
        Generates random shapes to a list of shapes(container)
        :param number_shapes: number of shapes to be in the list(container)
        :param min_edge: number from the main for min edge1
        :param max_edge: number from the main for max edge1
        print: the list of shapes
        """
        for i in range(0, number_shapes):
            shape = random.randint(0, 2)
            if shape == 0:
                edge1 = random.randint(min_edge, max_edge)
                edge2 = random.randint(min_edge, max_edge)
                colour = random.randint(1, 9)
                self.colour = LIST_COLOUR[colour]
                shape = Rectangle(self.colour, None, None, edge1, edge2)
                self.list_shapes.append(shape)
            elif shape == 1:
                radios = random.randint(min_edge, max_edge)
                colour = random.randint(1, 9)
                self.colour = LIST_COLOUR[colour]
                shape = Circle(self.colour, None, None, radios)
                self.list_shapes.append(shape)
            else:
                edge1 = random.randint(min_edge, max_edge)
                colour = random.randint(1, 9)
                self.colour = LIST_COLOUR[colour]
                shape = Square(self.colour, None, None, edge1)
                self.list_shapes.append(shape)
        for shape in self.list_shapes:
            print(f'The shape is: {shape}')

    def Sum_Areas(self):
        """
        Sums up the areas of all the shapes in the list(container)
        :return: sum of the areas
        """
        sum_areas = 0
        for shape in self.list_shapes:
            area = shape.Area_Calculation()
            sum_areas += area
        return f'The sum of the arrays: {sum_areas}'

    def Sum_Perimeters(self):
        """
        Sums up the perimeters of all the shapes in the list(container)
        :return: sum of the perimeters
        """
        sum_perimeter = 0
        for shape in self.list_shapes:
            perimeter = shape.Perimeter_Calculation()
            sum_perimeter += perimeter
        return f'The sum of the perimeters: {sum_perimeter}'

    def count_colours(self):
        """
        count how many times the same colours appears
        :return: the number os each colour appears
        """
        for colour in LIST_COLOUR:
            count = 0
            for shape in self.list_shapes:
                if shape.Get_Colour() == colour:
                    count += 1
            LIBRARY_COLOUR[colour] = count

        return LIBRARY_COLOUR
