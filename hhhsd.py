# Задание 1
name_film = input("Введите название фильма")
name_cinema = input("Введите название кинотеатра")
time = input("Введите время")
print(f'Билет на " {name_film} " в " {name_cinema} " на " {time} забронирован ')
# Задание 2
monthly_salary = int(input("Введите зарплату за месяц"))
worked_hours = int(input("Введите количество отработанных часов в выходные"))
award = monthly_salary * 0.01 * worked_hours
print("Размер премии:", award)
# Задание 3
sum = input("Введите сумму:"))
print(sum % 10, "- 1р")
print(sum % 100 // 10, "- по 10р")Я
print(sum % 1000 // 100, "- по 100р")
print(sum // 1000, "-по 1000р")
# Задание 4
feedback = input("Оцените развлекательный комплекс")
searching1 = feedback.find("весело")
searching2 = feedback.find("увлекательно")
searching3 = feedback.find("развлечения")
print("Результат анализа:", searching1, searching2, searching3)
# Задание 5