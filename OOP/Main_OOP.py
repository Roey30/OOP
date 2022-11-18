"""
 Author: Roey Firan
 Date: 30/9/2023
 Objects oriented program
 uses shape as main object and go down to
 rectangle and circle and from the rectangle to a square
 at the the you get number of random objects(shapes),
 the sum of their areas and perimeter and how much the same
 colour appeared in this group of random objects(shapes)
"""
# IMPORTS
from Shape_Storage import *
"from Shape import *"


def main():
    """
    The main function calls the Generates, Sum_Areas,
     Sum_Perimeters and count_colours functions
    """
    try:
        """
        Example code (I used it the check myself)
        shape1 = Shape('blue', 10, 20)
        shape1.Set_Colour('yellow')
        print("Shape1: ")
        print(f'The area is: {shape1.Get_Area()}, The color is: {shape1.Get_Colour()},'
              f' The perimeter is: {shape1.Get_Perimeter()}')
        shape1.Set_Colour('yellow')
        shape1.Set_Area(15)
        shape1.Set_Perimeter(30)
        print(f'The new area is: {shape1.Get_Area()}, The new color is: {shape1.Get_Colour()},'
              f' The new perimeter is: {shape1.Get_Perimeter()}')
        rectangle1 = Rectangle('red', None, None, 5, 6)
        print("Rectangle1: ")
        print(f'The edge1 is:  {rectangle1.Get_Edge1()}, The edge2:  {rectangle1.Get_Edge2()}')
        print(f'The area is: {rectangle1.Area_Calculation()}, The color is: {rectangle1.Get_Colour()},'
              f' The perimeter is: {rectangle1.Perimeter_Calculation()}')
        rectangle2 = Rectangle('red', None, None, 5, 8)
        print("Rectangle2: ")
        print(f'The edge1 is:  {rectangle2.Get_Edge1()}, The edge2:  {rectangle2.Get_Edge2()}')
        print(f'The area is: {rectangle2.Area_Calculation()}, The color is: {rectangle2.Get_Colour()},'
              f' The perimeter is: {rectangle2.Perimeter_Calculation()}')

        circle = Circle('black', None, None, 5)
        print("Circle: ")
        print(f'The radios is:  {circle.Get_Radios()}')
        print(f'The area is: {circle.Area_Calculation()}, The color is: {circle.Get_Colour()},'
              f' The perimeter is: {circle.Perimeter_Calculation()}')
        square1 = Square('green', None, None, 8)
        print("Square1: ")
        print(f'The area is: {square1.Area_Calculation()}, The color is: {square1.Get_Colour()},'
              f' The perimeter is: {square1.Perimeter_Calculation()}')
        square2 = Square('green', None, None, 5)
        print("Square2: ")
        print(f'The area is: {square2.Area_Calculation()}, The color is: {square2.Get_Colour()},'
              f' The perimeter is: {square2.Perimeter_Calculation()}')

        new_area = rectangle1.Combine_Shapes(rectangle2)
        print(f'The new area is(rectangle + rectangle): {new_area}')
        new_area = rectangle1.Combine_Shapes(square1)
        print(f'The new area is(rectangle + square): {new_area}')
        new_area = rectangle2.Combine_Shapes(square2)
        print(f'The new area is(rectangle + square): {new_area}')
        """

        my_container = Container()
        my_container.Generate(100, 1, 10)
        print("Total area: ", my_container.Sum_Areas())
        print("Total perimeter: ", my_container.Sum_Perimeters())
        print("Number of colours: ", my_container.count_colours())
    except ConnectionResetError and KeyboardInterrupt:
        print(f'There has been a problem please try again')
    finally:
        print('Thank you for using us good by')


if __name__ == '__main__':
    main()
