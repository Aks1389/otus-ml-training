alphabet = "abcdefghijklmnopqrstuvwxyz"

string = input("Введите строку сиволов:\n")
shift = None
while True:
    shift = input("Введите целочислленный ключ:\n")
    if shift.isdigit():
        shift = int(shift)
        break
output = ""

for letter in string:
    if letter.lower() in alphabet:
        letter_position = alphabet.index(letter.lower())
        shifted_index = letter_position + shift
        if shifted_index >= len(alphabet):
            shifted_index = abs(len(alphabet) - letter_position - shift)
        output += alphabet[shifted_index] if letter.islower() else alphabet[shifted_index].upper()
    else:
        output += letter
print(output)