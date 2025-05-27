from sort_tuples import sort_tuples
from map_example import map_example
from filter_example import filter_example


def main():
    print("Задача 1: Сортировка кортежей")
    tuples_list = [
        ("apple", 10, "banana"),
        ("kiwi", 5, "apple"),
        ("banana", 20, "kiwi"),
        ("peach", 15, "apple"),
    ]
    sorted_tuples = sort_tuples(tuples_list)
    print(sorted_tuples)

    print("\nЗадача 2: Map и Lambda")
    numbers = [1, 2, 3, 4, 5]
    mapped = map_example(numbers)
    print(list(mapped))

    print("\nЗадача 3: Filter и Lambda")
    filtered = filter_example(numbers)
    print(list(filtered))


if __name__ == "__main__":
    main()
