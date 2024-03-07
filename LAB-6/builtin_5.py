tuple1 = (True,False,True)
tuple2 = (True,True,True,True,True)
tuple3 = (1,1,1,1,2)
tuple4 = (1,1,1,1,0)
def check(tuple):
    if all(tuple):
        print("TRUE")
    else:
        print("FALSE")
check(tuple1)
check(tuple2)
check(tuple3)
check(tuple4)