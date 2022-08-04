from Class01 import *
from ex01 import *

사람들 = []
메뉴들 = []


def print_hi(name):
   a = Character("as",20)
   w = Warrior("as",28)
   w.Walk()
   w.info()
   w.attack()

   s= Shape(1,2)
   r=Rectangle(10,202)
   t=Triangle(2,3)
   print(s.getWidth())
   print(s.getHeight())
   print(r.calArea())
   print(t.calArea())

def 이야기초기화():
    등장인물 = 사람들[2]
    등장인물[0] = 점원1()
    등장인물[1] = 점원2()

    메뉴 = 메뉴들[3]
    메뉴[0] = 메뉴1()
    메뉴[1] = 메뉴2()
    

def 이야기시작():
        
    # 점원1.인사하다
    pass
    

if __name__ == '__main__':
    # print_hi("name")
    이야기초기화()
    이야기시작()
