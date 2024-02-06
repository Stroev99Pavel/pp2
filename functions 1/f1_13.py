import random
print("Hello! What is your name?")
name = input()
a = "Well, {}, I am thinking of number between 1 and 20 "
b = "Good job, {}! You guessed my number in {} guesses!"
print(a.format(name))
generated = random.randint(1,20)
print(generated)
print("Take a guess")
num = input()
num = int(num)
count = 1
def guess(n,generated,count):
    if n == generated:
        print(b.format(name,count))
        return 0
    else:
        count = count + 1
        print("Take a guess")
        num = input()
        num = int(num)
        guess(num, generated,count)
guess(num,generated,count)