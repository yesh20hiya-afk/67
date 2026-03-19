rowsize = int (input("Enter the number of rows: "))
if rowsize%2 == 0:
    halfdiamondrow = int(rowsize/2)
else:
    halfdiamondrow = int((rowsize/2)+1)

space = halfdiamondrow - 1
for i in range (1, halfdiamondrow+1):
    for j in range (space):
        print(" ", end="")
    space -= 1
    num = 1
    for k in range (2*i-1):
        print(num, end="")
        num = num + 1
    print()

space = 1
for i in range (1,halfdiamondrow):
    for j in range (space):
        print(" ", end="")
    space += 1
    num = 1
    for k in range (2*(halfdiamondrow-i)-1):
        print(num, end="")
        num = num + 1
    print()