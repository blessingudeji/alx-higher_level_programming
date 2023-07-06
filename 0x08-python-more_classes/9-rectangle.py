"""A class that defines a rectangle

"""


class Rectangle:
    """Initializes a rectangle object

    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def bigger_or_equal(rect_1, rect_2):
        """return biggest area of the rectangle

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """makes a square rectangle

        """
        return cls(size, size)

    @property
    def width(self):
        """get width

        """
        return self.__width

    @property
    def height(self):
        """get height

        """
        return self.__height

    @width.setter
    def width(self, value):
        """set width

        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """set height

        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """returns the area of rectangle

        """
        return self.width * self.height

    def perimeter(self):
        """ returns the perimeter of rectangle

        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ modifies the string

        """
        if self.width == 0 or self.height == 0:
            return ""
        return '\n' .join('#' * self.width for _ in range(self.height))

    def __repr__(self):
        return("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """ modifies del object

        """
        Rectangle.number_of_instances -= 1
        print("{}".format("Bye rectangle..."))
