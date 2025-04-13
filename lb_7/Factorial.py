def factorial(z):
    if z == 0 or z == 1:
        return 1
    return z * factorial(z - 1)