number = None
while True:
    number = input("Введите арабское число\n")
    if number.isdigit():
        number = int(number)
        break
dictionary = {1: "I", 5 : "V", 10 : "X", 50 : "L", 100 : "C", 40 : "XL", 9 : "IX", 4 : "IV", 90 : "XC"}
nums = [100, 90, 50, 40, 10, 9, 5, 4, 1]
rem = number
s = ''
for i in nums:
    while i<=rem:
        rem-=i
        s+=dictionary[i]
print(s)