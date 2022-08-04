class Shape:
    def __init__(self,width,height):
        self.__width = width
        self.__height = height

    def getWidth(self):
        return self.__width
    def getHeight(self):
        return self.__height

    def setWidth(self,w):
        self.__width = w
    def setHeight(self,h):
        self.__height = h

    def calArea(self):
        return 0

class Rectangle(Shape):
    def calArea(self):
        return int(self.getHeight())*int(self.getWidth())

class Triangle(Shape):
    def calArea(self):
        return int(self.getWidth() * self.getHeight() /2)


