pages = ["HOME"]
cmd_count = int(input())
index = 0

for _ in range(cmd_count):
    command = input()

    if command == "forward":
        if index == len(pages) - 1:
            print(pages[-1])
        else:
            index += 1
            print(pages[index])

    elif command == "backward":
        if index == 0:
            print(pages[0])
        else:
            index -= 1
            print(pages[index])

    else:
        pages.append(input())
        print(pages[-1])
