def repeatedString(s, n):
    frequency = s.count('a')

    result = n // len(s) * frequency
    result += s[:n % len(s)].count('a')

    return result


s = input()
n = int(input())
print(repeatedString(s, n))
