    def main():

        a = ""
        for _ in range(8):
            a += input()
        print(a)

        n = int(input())
        names = []
        for _ in range(n):
            names.append(input())
        for i in range(n):
            print(f"{names[i]} {i + 1}")

            day_start = int(input())
            m = int(input())
            dates = [str(i) for i in range(day_start, 32, m) if i <= 31]
            print(" ".join(dates))

        letter = input()
        count = int(input())
        max_count = 0
        current_count = 0
        for i in range(count):
            char = input()
            if char == letter:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
        print(max_count)

        number = int(input())
        sum_divisors = 0
        for i in range(1, number + 1):
            if number % i == 0:
                sum_divisors += i
        print(number, sum_divisors)

        text = input()
        vowels = "аяоёэеуюыи"
        unstressed_vowels = 0
        for i in range(len(text)):
            if text[i] in vowels:
                if i == 0 or text[i - 1] == " ":
                    unstressed_vowels += 1
        print(unstressed_vowels)

        word = input()
        n = int(input())
        for i in range(1, n + 1):
            print(word * i)

            phone_number = input()
            for i in phone_number:
                if not (i.isdigit() or i == "+"):
                    print("Неправильный номер телефона!")
                    break
                else:
                    print("Авторизация по номеру телефона успешна!")

        password = input()
        vowels = "аеёиоуыэюя"
        encrypted_password = ""
        for i in password:
            if i.lower() in vowels:
                encrypted_password += "0"
            else:
                encrypted_password += "1"
        print(encrypted_password)

        message = 'ППррииввеетт!!  ККаакк  ддееллаа??  ССееггоодднняя  ттааккааяя  ххоорроошшааяя  ппооггооддаа,,  ммоожжеетт  ппооггуулляяеемм??'
        corrected_message = ""
        for i in range(len(message)):
            if i % 2 == 0:
                corrected_message += message[i]
        print(corrected_message)

    if __name__ == "__main__":
        main()