class Upper:
    def __init__(self):
        self.str = str
    def getString(self):
        str = input()
        return str
    def printString(self,str):
        print(str.upper())

x = Upper()
s = x.getString()
x.printString(s)