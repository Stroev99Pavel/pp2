from time import sleep
import math
num = 9
print("How many milliseconds you want to wait?")
milliseconds = int(input())
seconds = milliseconds / 1000
sleep(seconds)
print(math.sqrt(num))