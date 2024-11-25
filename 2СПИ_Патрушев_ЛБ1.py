    def main():

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
    print(sum % 100 // 10, "- по 10р")
    Я
    print(sum % 1000 // 100, "- по 100р")
    print(sum // 1000, "-по 1000р")

    # Задание 4

    feedback = input("Оцените развлекательный комплекс")
    searching1 = feedback.find("весело")
    searching2 = feedback.find("увлекательно")
    searching3 = feedback.find("развлечения")
    print("Результат анализа:", searching1, searching2, searching3)

    # Задание 5

    word = input()
    print(word[(len(word) - 1) // 2])

    # Задание 6

    feedback = 'Алиса и Вася, большое спасибо за теплый приём!'
    name1 = feedback[0:5]
    name2 = feedback[8:12]
    print('Назначить премию:', name1 + '/' + name2)

    # Задание 7

    while True:
    n = int(input('n = '))
    s = ' '
    for i in range(n - 1, n + 3):
    s += chr(ord('A') + i % 26)
    print(s)

    # Задание 8

    my_list = [1, 2, 3, 4, 5]
    my_list.append(6)
    my_list.insert(0,0)
    my_list.remove(3)
    del my_list[0]
    slice = my_list[1:4]
    reversed_list = my_list[::-1]
    my_list.reverse()
    two_dimensional_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    my_list.clear()

    # Задание 9

    empty_tuple = ()
    filled_tuple = (1, 2, 3, 4, 5)
    print(empty_tuple)
    print(filled_tuple)

    # Задание 10

    empty_set = set()
    my_set = {1, 2, 3, 4, 5}
    empty_set.add(6)
    empty_set.add(7)
    union_set = my_set.union(empty_set)
    intersection_set = my_set.intersection(empty_set)
    difference_set = my_set.difference(empty_set)

    # Задание 11

    my_dict = {}
    my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
    my_dict['email'] = 'john@example.com'
    del my_dict['city']
    my_dict['age'] = 31

    if __name__ == "__main__":
        main()