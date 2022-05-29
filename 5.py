def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if not x % i:
            return False
    return True


start = int(input("Enter the lower bound value : "))
end = int(input("Enter the upper bound value : "))

print(f"The prime numbers between {start} and {end} are :", end=" ")

if 2 >= start:
    print(2, end=" ")

if not start % 2:
    start += 1

for i in range(start, end + 1, 2):
    if is_prime(i):
        print(i, end=" ")
