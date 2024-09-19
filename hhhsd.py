name_film = input("Введите название фильма")
name_cinema = input("Введите название кинотеатра")
time = input("Введите время")
print(f'Билет на " {name_film} " в " {name_cinema} " на " {time} забронирован ')

monthly_salary = int(input("Введите зарплату за месяц"))
worked_hours = int(input("Введите количество отработанных часов в выходные"))
award = monthly_salary * 0.01 * worked_hours
print("Размер премии:", award)
