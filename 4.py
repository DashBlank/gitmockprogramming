for i in range(6):
    for j in range(1, i):
        print(j, end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
