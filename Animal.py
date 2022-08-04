class Animal :

    def __init__(self, name = None, age = None):
        if name == None :
            self.name = "이름이 없어요!"
        if age == None : 
            self.age = "나이를 모르겠어요!"
            return
        self.name = name
        self.age = age

    def setInfo(self):
        print("이름은 뭔가요?")
        self.name = input()
        print("나이는 몇 살인가요?")
        self.age = input()
    def __del__(self):
        print("{}가 없어졌어요!" .format(self.name))

cat = Animal("popi", 2)
dog = Animal()

print(cat.name)
print(dog.name)
del cat
dog.setInfo()
print(dog.name)