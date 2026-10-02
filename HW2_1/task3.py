minutes = int(input("Введіть кількість хвилин: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print(hours, "години", remaining_minutes, "хвилин")