# module only to contain functions to compute the area of a circle, rectangle, square, triangle
def circle_area(radius):

    area = ((radius * radius)*(3.14))
    return area

def rect_area(length, width):

    area = (length * width)
    return area

def square_area(side):

    area = (side * side)
    return area

def tri_area(side_1, side_2):

    area = ((side_1 * side_2)/2)
    return area


