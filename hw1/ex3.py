size = input("Введите размер плитки шоколада(х:у)\n")
cut_size = input("Введите размер отламливаемого куска\n")
length, width = list(map(int, size.split(':')))
possible = int(cut_size) % int(length) == 0 \
    or int(cut_size) % int(width) == 0 \
    and int(cut_size) <= length * width
print(size + ', ' + cut_size + ': ' + str(possible))