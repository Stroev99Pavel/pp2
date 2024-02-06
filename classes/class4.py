import math
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def show(self):
        print(self.x)
        print(self.y)
    def move(self):
        print("Give new x and y")
        x = input()
        y = input()
        self.x = int(x)
        self.y = int(y)
    def dist(self, second):
        a = abs(math.sqrt((self.x - second.x)**2 + (self.y - second.y)**2))
        return a
F = Point(2, 5)
S = Point(1, 4)
F.show()
S.show()
print(F.dist(S))