    def main():

    # Задание 1

    str = input()
    if str == 'Python':
    print('ДА')
    else:
    print('НЕТ')

    # Задание 2

    word1 = input("Введите слово:")
    word2 = input("Введите слово:")
    if word1 == "да" and word2 == "да":
        print("ВЕРНО")
    elif word1 == "нет" and word2 == "нет":
        print("ВЕРНО")
    else:
        print("НЕВЕРНО")

    # Задание 3

    str1 = input()
    str2 = input()
    str3 = input()
    if (str1 == '1' or str1 == 'раз') and (str2 == '2' or str2 == 'два') and (str3 == '3' or str3 == 'три')
        print('ГОРИ')
    else:
        print('НЕ ГОРИ')

    # Задание 4

    city1 = input("Введите город:")
    city2 = input("Введите город:")
    if city1 == "Тула" or city2 == "Пенза":
        print("ДА")
    else:
        print("НЕТ")

    # Задание 5

    distance = int(input())
    day_distance = int(input())
    finish = distance // day_distance
    if distance % day_distance != 0:
        finish += 1
    print(finish)

    # Задание 6

    num = int(input("Введите трехзначное число:"))
    num1 = num // 100
    num2 = num // 10 % 10
    num3 = num % 10
    sum = num1 + num3
    if sum % 8 == 0 and num2 != 3:
        print("НЕПОДХОДИТ", sum, num2)
    else:
        print("ПОДХОДИТ:", sum, num2)

    # Задание 7

    category = input('Категория:')
    if category == 'продукты':
        sum = int(input('Цена:'))
        if sum < 100:
            print('Попробуйте нашу выпечку!')
        elif 99 < sum < 500:
            print('Как насчёт орехов в шоколаде?')
        elif sum > 499:
            print('Попробуйте экзотические фрукты!')
    elif category != 'продукт':
        print('Загляните в товары для дома!')

    # Задание 8

    product1 = int(input('Цена первого товара:'))
    product2 = int(input('Цена второго товара:'))
    product3 = int(input('Цена третьего товара:'))
    if product1 < product2 < product3:
        print('Акция!')
        print('К оплате:', (product1 + product2 + product3) / 2 )
    elif product1 > product2 > product3:
        print('Акция!')
        print('К оплате:', (product1 + product2 + product3) / 3)
    else:
        print('К оплате:', product1 + product2 + product3)

    # Задание 9

    client1 = int(input('Введите число покупателей за позавчера:'))
    client2 = int(input('Введите число покупателей за вчера:'))
    if client2 > client1:
        print('Сегодня магазин посетит:', client2 + (client2 - client1), 'человек')
    elif client2 < client1:
        print('Сегодня магазин посетит:', client2 - (client2 - client1), 'человек')

    # Задание 10

    year = int(input())
    if year % 4 == 0 and (year % 400 == 0 or year % 100):
        print('Високосный')
    else:
        print('Не високосный')

    # Задание 11

    num = int(input())
    if num % 2 == 0:
        print('Четное')
    else:
        print('Нечетное')


    if __name__ == "__main__":
        main()