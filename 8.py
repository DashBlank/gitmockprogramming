string = input()
is_consecutive = True
while is_consecutive:
    is_consecutive = False
    start = 0
    end = 0
    while start < len(string) - 2:
        while end < len(string) and string[start] == string[end]:
            end += 1

        if end - start >= 2:
            is_consecutive = True
            string = string[:start] + string[end:]
            break
        else:
            start += 1
            end = start
print("\"", string, "\"", sep="")
