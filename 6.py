size = int(input())
names = [input() for _ in range(size)]
names.sort()
print()
for name in names:
    print(name)
