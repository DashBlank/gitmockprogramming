numbers = list(map(int, input().split()))
numbers = list(sorted(numbers[:len(numbers)//2])) + list(sorted(numbers[len(numbers)//2:], reverse=True))
print(numbers)