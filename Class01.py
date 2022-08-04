from unicodedata import name


class Character:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    
    def Walk(self):
        print("이동")
    def attack(self):
        print("공격")

class Warrior(Character):
    def __init__(self):
        self.이름 = "a"
    def info(self):
        print("전사")
    def attack(self):
        print("강한공격")

class 사람:
    def __init__(self,이름):
        self.이름 = 이름
    def 인사하다(self):
        print("안녕하세요")


class 고객1(사람):
    pass
class 고객2(사람):
    pass
class 고객3(사람):
    pass

class 메뉴:
    pass

class 메뉴1(메뉴):
    pass

class 메뉴2(메뉴):
    pass

class 메뉴3(메뉴):
    pass

class 점원1(사람):
    def __init__(self, 이름):
        self.이름 = "사장"
    
class 점원2(사람):
    이름 = "편의점직원"
class 점원3(사람):
    이름 = "점원"


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




