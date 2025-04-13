def count_vowels(s, index=0):
    vowels = "аеёиоуыэюяAEIOUYaeiouy"
    if index == len(s):
        return 0
    return (1 if s[index] in vowels else 0) + count_vowels(s, index + 1)