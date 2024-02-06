def histogram(lists):
    lenght = len(lists)
    i = 0
    while i < lenght:
        j = 0
        while j < lists[i]:
            print("*",end="")
            j = j + 1
        print("")
        i = i + 1

histogram([1, 5, 1, 2])
histogram([1, 2, 3, 4, 5, 6])