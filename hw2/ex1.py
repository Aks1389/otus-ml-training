number = None
while True:
    number = input("Введите число:\n")
    if number.isdigit():
        break
while len(number) > 1:
    sum = 0
    for i in range(len(number)):
        sum += int(number[i])
    number = str(sum)
print(number)