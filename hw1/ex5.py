import re

# Способ 1
number = input("Введите число\n")
regex = re.compile(r"^-?\d*(\.\d+)?$")
is_real = regex.fullmatch(number) is not None
print(number + " вещественное: " + str(is_real))

# Способ 2
try:
    float(number)
    is_real = True
except ValueError:
    is_real = False
finally:
    print(number + " вещественное: " + str(is_real))

    