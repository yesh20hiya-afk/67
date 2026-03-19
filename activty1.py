print("Make your own star pyramid!")
n = int(input("how many levels of stars do you want?"))

for i in range (n):
    for j in range (i+1):
        print("*", end="")
    print()