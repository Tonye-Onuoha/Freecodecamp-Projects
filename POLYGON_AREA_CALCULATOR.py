class Rectangle:
    def __init__(self,width,height):
        self.width  = width
        self.height = height

    def set_width(self,new_width):
        """Sets new width"""
        self.width = new_width

    def set_height(self,new_height):
        """Sets new height"""
        self.height = new_height

    def get_area(self):
        """Returns area (width * height)"""
        return self.width * self.height

    def get_perimeter(self):
        """Returns perimeter (2 * width + 2 * height)"""
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        """Returns diagonal ((width ** 2 + height ** 2) ** .5)"""
        return ((self.width ** 2 + self.height ** 2) ** 0.5)

    def get_picture(self):
        """Returns a string that represents the shape using lines of "*".
        The number of lines should be equal to the height and the number of "*"
        in each line should be equal to the width.
        There should be a new line (\n) at the end of each line.
        If the width or height is larger than 50, this should return the string:
        "Too big for picture."."""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = []
        for i in range(self.height):
            line = ("*" * self.width) + "\n"
            picture.append(line)

        image = "".join(picture)
        return image

    def get_amount_inside(self,instance):
        """Takes another shape (square or rectangle) as an argument.
        Returns the number of times the passed in shape could fit
        inside the shape (with no rotations)."""
        amount = self.get_area()//instance.get_area()
        return amount

    def __str__(self):
        """Returns string representation of instance"""
        return "Rectangle(width={}, height={})".format(self.width,self.height)

class Square(Rectangle):
    def __init__(self,side_length):
        width = side_length
        height = side_length
        super().__init__(width,height)

    def set_side(self,value):
        self.width  = value
        self.height = value

    def set_width(self,new_width):
        self.set_side(new_width)

    def set_height(self,new_height):
        self.set_side(new_height)

    def __str__(self):
        return "Square(side={})".format(self.width)
