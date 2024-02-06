class Shape:
    def __init__(self,ar = 0):
        self.area = ar
    def Area(self,l = 0):
        ar = l*l
        print(ar)
class Rectangle(Shape):
    def __init__(self,length = 0,width = 0):
        self.length = length
        self.width = width
    def inpL(self):
        length = input()
        self.length = int(length)
    def inpW(self):
        width = input()
        self.width = int(width)
    def CalcArea(self):
        print(self.length * self.width)
New = Rectangle()
New.inpL()
New.inpW()
New.CalcArea()

