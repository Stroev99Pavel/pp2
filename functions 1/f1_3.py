def solve(numheads, numlegs): #h=35 l=94
    rabbits = (numlegs - 2 * numheads) / 2
    chickens = (numheads - rabbits)
    print("r=",rabbits)
    print("c=",chickens)
solve(35,94)