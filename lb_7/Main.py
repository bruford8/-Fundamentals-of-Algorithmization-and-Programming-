from factorial import factorial
from fibonacci import fibonacci
from count_vowels import count_vowels
from is_prime import is_prime
from find_max import find_max

def main():
    num1 = 5
    print(factorial(num1))
    num2 = 10
    print(fibonacci(num2))
    text = ("Why are we still here? Just to suffer? Every night,"
            " I can feel my leg... And my arm... even my fingers..."
            " The body I've lost... the comrades I've lost... won't stop hurting..."
            " It's like they're all still there."
            " You feel it, too, don't you? I'm gonna make them give back our past!")
    print(count_vowels(text))
    num = 10
    print(is_prime(num))
    numbers = [3, 7, 2, 9, 4, 10, 6]
    print(find_max(numbers))

if __name__ == '__main__':
    main()