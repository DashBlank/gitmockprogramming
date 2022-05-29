n, k = map(int, input().split())
array = list(map(int, input().split()))

index = k % n
e = 100

while index:
    if array[index]:
        e -= 2
    e -= 1
    index = (index + k) % n
else:
    e = e - (3 if array[0] else 1)

print(e)
