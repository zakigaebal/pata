#1-2 first.py
class addition:
    def __init__(self, a, b):
        self.a = a
        self.b =b
    def add(self):
        result = self.a + self.b
        return result
if __name__=="__main__":
    print(addition(1,2).add())
    print(__name__)
else:
    print(__name__)