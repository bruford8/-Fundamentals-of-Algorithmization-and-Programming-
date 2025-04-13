def fibonacci(v):
    if v <= 0:
        return "Некорректный ввод"
    elif v == 1:
        return 0
    elif v == 2:
        return 1
    return fibonacci(v - 1) + fibonacci(v - 2)