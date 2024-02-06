def unique(lists):
    lists.sort()
    i = 0
    new = []
    while i < len(lists) - 1:
        if lists[i] != lists[i+1]:
            new.append(lists[i])
            if i+2 == len(lists):
                new.append(lists[i+1])
        i = i + 1
    print(new)


unique([1,1,2,2,3,3,1,2,3,4,6])
unique([12,3,4,2,5,5,5,5,3,21,12,3])