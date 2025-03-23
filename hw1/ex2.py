n = None
while True:
    n = input("Введите число дней до отпуска\n")
    if n.isdigit():
        n = int(n)
        break
week = 7
weekend_length = 2
full_weeks = n // week
days_in_last_week = n - (week * full_weeks)
working_days_left_in_last_week = week - weekend_length - days_in_last_week
if (working_days_left_in_last_week) > 0:
     weekends_in_last_week = 0
else:
    weekends_in_last_week = abs(working_days_left_in_last_week)
weekends_until_vac = weekend_length * full_weeks + weekends_in_last_week
print(str(n) +" --> "+str(weekends_until_vac))