password = input()
alphabet = False
digit = False
special = False

for character in password:
    if 'A' <= character.upper() <= 'Z':
        alphabet = True
    elif '0' <= character <= '9':
        digit = True
    else:
        special = True

if alphabet:
    if digit:
        if special:
            print("Strong Password.")
        else:
            print("Moderate Password.")
    else:
        print("Weak Password.")

