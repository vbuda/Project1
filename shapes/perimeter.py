# module only to contain functions to compute the perimeter of a circle, rectangle, square, triangle
def circle_perim(radius):

    perim = (2 * 3.14 * radius)
    return perim

def rect_perim(length, width):

    perim = (length + width) * 2
    return perim

def square_perim(side):

    perim = (side) * 4
    return perim

def tri_perim(side_1, side_2, side_3):

    perim = (side_1 + side_2 + side_3)
    return perim

