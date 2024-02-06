def filter_prime(num):
    i = 0
    while i < len(num):
        tmp = 0
        n = num[i]
        n = int(n)
        for x in range(10):
            if x == 0:
                continue
            if (n % x) == 0:
                tmp = tmp+1
        i = i + 1
        if tmp < 3 :
            print(n)
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filter_prime(L)

