def convert_size(size_bytes):
    units = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
    index = 0
    while size_bytes >= 1024 and index < len(units) - 1:
        size_bytes /= 1024
        index += 1
    return f"{size_bytes:.2f} {units[index]}"

try:
    with open('input.txt', 'r', encoding='utf-8') as file:
        text = file.read()
        char_count = len(text)
        size_bits = char_count * 8  # Размер в битах (1 символ = 8 бит)
        size_bytes = char_count  # Размер в байтах (1 символ = 1 байт)

        print(f"Количество символов: {char_count}")
        print(f"Размер в битах: {size_bits} бит")
        print(f"Размер в байтах: {size_bytes} Б")
        print(f"Размер в максимально возможных единицах: {convert_size(size_bytes)}")
except FileNotFoundError:
    print("Файл input.txt не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")