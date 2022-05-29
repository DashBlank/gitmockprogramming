number = list(input())
for i in range(len(number)):
    number[i] = str((int(number[i]) + 1) % 10)
print("".join(number))

