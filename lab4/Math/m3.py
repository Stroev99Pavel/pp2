import math
#Input number of sides: 4
#Input the length of a side: 25
#The area of the polygon is: 625
a = 25
n = 4
tang = math.tan(180/n)
apothem = a/(2 * tang)
P = a * n
Area = P * apothem / 2
print(Area)