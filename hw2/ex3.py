string = input("Введите строку сиволов:\n")

output = ""
counter = 0
for i in range(len(string)):
    counter += 1
    if i < len(string)-1:
        if string[i] != string[i+1]:
            output += f"{counter}{string[i]}"
            counter = 0
    else:
        output += f"{counter}{string[i]}"
print(output)