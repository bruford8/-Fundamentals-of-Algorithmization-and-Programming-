    def main():

    # Задание 1

     while True:
         x = input("Введите строку:")
         if x == "":
             break
         print("Длина этой строки:", len(x))

     # Задание 2

     count = 0
     while True:
         x = float(input("Введите число:"))
         if x > 36.6:
             break
         elif x <= 36.6:
             count += 1
     print("Количество отрицательных чиел:", count)

     # Задание 3

     first_max = 0
     second_max = 0
     while True:
         num = int(input("Введите число: "))
         if abd(num) >= 1000:
             break
         if

     # Задание 4

     num = input("Введите числа через пробел: ")
     num_list = num.split(" ")
     num_list = list(map(float, num_list))
     min_num = num_list[0]
     counter = 1
     while counter < len(num_list):
         if num_list[counter] < min_num:
             min_num = num_list[counter]
         counter += 1
     print(min_num)

     # Задание 5

     num = float(input("Введите число: "))
     while True:
         if num == 0:
             break
         elif num % 3 == 0 and num % 7 == 0:
             print("Караул!")
             break
         elif num % 3 == 0 and num % 7 != 0:
             print("Несчастливое")
         elif num % 7 == 0 and num % 3 != 0:
             print("Опасное")
         else:
             print(num)
         num = float(input("Введите число: "))

     # Задание 6

     a = 0
     num = 1
     while num <= 10000:
         if num % num == 0 and num % 1 == 0:
             a += num
             num += 1
         else:
             break
     print(a)

     # Задание 7

     # Задание 8

     word = [input("Введите слово: ")]
     small_word = [word[0]]
     while word[-1] != "стоп":
         if len(word[-1]) < len(small_word[-1]):
             small_word = [word[-1]]
         word.append(input("Введите слово: "))
     print(small_word[0])

     # Задание 9

     num = float(input("Введите число: "))
     operator = input("Введите операцию: ")
     result = num
     while operator != "стоп":
         num = float(input("Введите число: "))
         if operator == "+":
             result += num
         elif operator == "-":
             result -= num
         elif operator == "*":
             result *= num
         elif operator == "/":
             result /= num
         elif operator == "**":
             result **= num
         print(result)
         operator = input("Введите операцию: ")

     # Задание 10

     result = ""
     while True:
         word = input("Введите слово или !: ")
         if word == "стоп":
             break
         result += word + " "
         if word == "!":
             result = result[:-3] + "!"
             result += "\n"
     print(result)


    if __name__ == "__main__":
        main()