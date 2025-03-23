number = None
while True:
    number = input("Введите пятизначное число\n")
    if len(number) == 5:
        break
new_number = number[0] + number[1:4][::-1] + number[len(number)-1]
print(number + " --> " + new_number)