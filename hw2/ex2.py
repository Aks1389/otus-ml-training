cinema_hall_1 = [[0,0,1,0], [1,1,0,1], [1,0,0,1], [0,0,0,1]]
cinema_hall_2 = [[1,1,1,0], [1,0,0,0], [0,0,0,0], [1,1,1,1]]
cinema_hall_3 = [[0,1,0,1], [1,0,1,0], [0,1,1,0], [0,0,1,1]]

tickets = int(input("Введите кол-во билетов:\n"))

cinema_hall = cinema_hall_3

row = None
for i in range(len(cinema_hall)):
    max_free_seats_sequence = 0
    free_seats = 0
    for j in range(len(cinema_hall[i])):
        if cinema_hall[i][j] == 0:
            free_seats += 1
        elif free_seats > max_free_seats_sequence:
            max_free_seats_sequence = free_seats
            free_seats = 0
    if free_seats > max_free_seats_sequence:
        max_free_seats_sequence = free_seats
    if max_free_seats_sequence >= tickets:
        row = i + 1
        break
else:
    row = False
print(f"Зал:{cinema_hall}, Кол-во мест: {tickets}, Подходящий ряд: {row}")