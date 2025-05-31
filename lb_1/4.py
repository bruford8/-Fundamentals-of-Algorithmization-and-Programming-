max_length = 0
longest_words = []

try:
    with open('words.txt', 'r', encoding='utf-8') as file:
        for line in file:
            word = line.strip()
            if len(word) > max_length:
                max_length = len(word)
                longest_words = [word]
            elif len(word) == max_length:
                longest_words.append(word)
except FileNotFoundError:
    print("Файл words.txt не найден.")
    exit()

if longest_words:
    if len(longest_words) == 1:
        print(longest_words[0])
    else:
        print(longest_words)
else:
    print("Файл пуст.")