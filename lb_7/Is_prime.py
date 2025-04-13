def is_prime(m, o=2):
    if m < 2:
        return False
    if o * o > m:
        return True
    return False if m % o == 0 else is_prime(m, o + 1)