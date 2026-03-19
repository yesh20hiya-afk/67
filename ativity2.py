print("Make your own star pyramid!")
n = int(input("how many levels of stars do you want?"))
count = 0
for i in range (n):
    for j in range (i+1):
        count += 1

        print(count, end=" ")
    print()