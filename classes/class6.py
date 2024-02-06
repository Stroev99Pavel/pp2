def prime(num):
    for i in range(2,int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num = [1,2,3,4,5,6,6,7,9,111,2,11,23,35,17]
num1 = [4,6,8,10,12,14]
prime_numbers = list(filter(lambda x: prime(x), num))
prime_numbers1 = list(filter(lambda x: prime(x), num1))
print(prime_numbers)
print(prime_numbers1)