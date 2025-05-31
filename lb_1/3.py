even_lines = []
odd_lines = []

try:
    with open('lines_random.txt', 'r', encoding='utf-8') as file:
        for index, line in enumerate(file):
            if index % 2 == 1:
                even_lines.append(line.strip())
            else:
                odd_lines.append(line.strip())
except FileNotFoundError:
    print("Файл lines.txt не найден.")
    exit()

print("Четные строки:")
print('\n'.join(even_lines))

print("Нечетные строки:")
print('\n'.join(odd_lines))