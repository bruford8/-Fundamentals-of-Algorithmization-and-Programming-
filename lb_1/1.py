import random

with open('lines_random.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

if lines:
    random_line = random.choice(lines)
    print(random_line)
else:
    print("Файл пуст.")

