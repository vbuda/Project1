import shapes.area as area
import shapes.perimeter as perimeter

class Circle:

    def __init__(self, radius: float) -> None:

        self.radius = radius

    def area(self) -> str:
        '''
        Function to compute area of a circle given the radius.
        :param radius: The radius of the circle.
        :return: Pi multiplied by the radius squared.
        '''
        return(f'Circle Area = {(self.radius * self.radius)*(3.14)}')

    def perimeter(self) -> str:
        '''
        Function to compute the perimeter of a circle given the radius.
        :param radius: The radius of the circle.
        :return: Two times pi times the radius.
        '''
        return(f'Circle perimeter = {(2 * 3.14 * self.radius)}')

class Rectangle:
    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def area(self) -> str:
        '''
        Function to compute area of a rectangle give the length and width.
        :param length: The length of the rectangle.
        :param width: The width of the rectangle.
        :return: Length multiplied by width.
        '''
        return(f'Rectangle area = {(self.length * self.width)}')

    def perimeter(self) -> str:
        '''
        Function to compute the perimeter of a rectangle given the length and width.
        :param length: The length of the rectangle.
        :param width: The width of the rectangle.
        :return: Length multiplied by width.
        '''
        return(f'Rectangle perimeter = {(self.length + self.width) * 2}')

class Square:
    def __init__(self, length: float) -> None:
        self.length = length

    def area(self) -> str:
        '''
        Function to compute the area of a square given one side.
        :param side: The length of the square.
        :return: The side squared
        '''
        return(f'Square area = {(self.length * self.length)}')

    def perimeter(self) -> str:
        '''
        Function to compute the perimeter of a square given the side.
        :param side: The side of the square.
        :return: The side multiplied by four.
        '''
        return(f'Square perimeter = {(self.length) * 4}')

class Triangle:
    def __init__(self, side_1: float, side_2: float, side_3: float) -> None:

        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def area(self) -> str:
        '''
        Function to compute the area of a triangle given two sides.
        :param side_1: The base of the triangle.
        :param side_2: The height of the triangle.
        :return: Base multiplied by height divided by two
        '''
        return(f'Triangle area = {(self.side_1 * self.side_2)/2}')

    def perimeter(self) -> str:
        '''
        Function to compute the perimeter of a triangle given 3 sides.
        :param side_1: The base of the triangle.
        :param side_2: One side of the triangle.
        :param side_3: Other side of the triangle.
        :return:
        '''
        return(f'Triangle perimeter = {(self.side_1 + self.side_2 + self.side_3)}')




def selection():
    try:
        print('----------------------')
        print('SELECT SHAPE')
        print('----------------------')
        print('1 - Circle')
        print('2 - Rectangle')
        print('3 - Square')
        print('4 - Triangle')

        # Code to check that a valid shape has been selected
        shape = int(input('Shape number: '))
        while shape < 1 or shape > 4:
            shape = int(input('Shape number (1-4): '))
        return shape
    except ValueError:
        print('----------------------')
        print('invalid input')


def formula():

    formula = (input('Computation (Area = 1 or Perimeter = 2): '))
    while formula != '1' and formula != '2':
        formula = (input('Enter 1 or 2: '))
    return int(formula)




def loop_break():
    ask = input('Continue (y/n): ').strip().lower()
    while ask != 'y' and ask != 'n':
        ask = input('Enter y or n: ').strip().lower()
    return ask


def main():
    while True:

        shape_choice = selection()

        # part 3
        if shape_choice == 1:
            formula_choice = formula()
            if formula_choice == 1:

                while True:
                    try:
                        radius = float(input('Circle radius: '))
                        circle = Circle(radius)
                        print(circle.area())
            #             print(f'Circle area = {area.circle_area(radius):.2f}')
                        break
                    except ValueError:
                        print('Enter numbers only')
            else:

                while True:
                    try:
                        radius = float(input('Circle radius: '))
                        circle = Circle(radius)
                        print(circle.perimeter())
                        # print(f'Circle perimeter = {perimeter.circle_perim(radius):.2f}')
                        break
                    except ValueError:
                        print('Enter numbers only')

            ask = loop_break()
            if ask == 'n':
                print('PROGRAM DONE')
                break

        elif shape_choice == 2:
            formula_choice = formula()
            if formula_choice == 1:
                while True:
                    try:
                        length = float(input('Rectangle length: '))
                        width = float(input('Rectangle width: '))
                        rectangle = Rectangle(length, width)
                        print(rectangle.area())
                       # print(f'Rectangle area = {area.rect_area(length, width):.2f}')
                        break
                    except ValueError:
                        print('Enter numbers only')
            else:
                while True:
                    try:
                        length = float(input('Rectangle length: '))
                        width = float(input('Rectangle width: '))
                        rectangle = Rectangle(length, width)
                        print(rectangle.perimeter())
                       # print(f'Rectangle perimeter = {perimeter.rect_perim(length, width):.2f}')
                        break
                    except ValueError:
                        print('Enter numbers only')
            ask = loop_break()
            if ask == 'n':
                print('PROGRAM DONE')
                break

        elif shape_choice == 3:
            formula_choice = formula()
            if formula_choice == 1:
                while True:
                    try:
                        side = float(input('Square length: '))
                        square = Square(side)
                        print(square.area())
                       # print(f'Square area = {area.square_area(side):.2f}')
                        break
                    except ValueError:
                        print('Enter numbers only')
            else:
                while True:
                    try:
                        side = float(input('Square length: '))
                        square = Square(side)
                        print(square.perimeter())
                        #print(f'Square perimeter = {perimeter.square_perim(side):.2f}')
                        break
                    except ValueError:
                        print('Enter numbers only')
            ask = loop_break()
            if ask == 'n':
                print('PROGRAM DONE')
                break

        elif shape_choice == 4:
            formula_choice = formula()
            if formula_choice == 1:
                while True:
                    try:
                        side_1 = float(input('Triangle side 1: '))
                        side_2 = float(input('Triangle side 2: '))
                        triangle = Triangle(side_1, side_2, side_3=1)
                        print(triangle.area())
                        #print(f'Triangle area = {area.tri_area(side_1, side_2):.2f}')
                        break
                    except ValueError:
                        print('Enter numbers only')

            else:
                while True:
                    try:
                        side_1 = float(input('Triangle side 1: '))
                        side_2 = float(input('Triangle side 2: '))
                        side_3 = float(input('Triangle side 3: '))
                        triangle = Triangle(side_1, side_2, side_3)
                        print(triangle.perimeter())
                        #print(f'Triangle perimeter = {perimeter.tri_perim(side_1, side_2, side_3):.2f}')
                        break
                    except ValueError:
                        print('Enter numbers only')

            ask = loop_break()
            if ask == 'n':
                print('PROGRAM DONE')
                break

if __name__ == '__main__':
    main()