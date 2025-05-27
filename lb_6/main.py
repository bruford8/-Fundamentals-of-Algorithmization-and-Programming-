from geometry import quarters
from universe import future
from electricity import circuit_resistance


def main():
    points = [(1, 2), (-1, 3), (4, -2), (-3, -4), (0, 5), (2, 0)]
    print("Четверти:", quarters(*points))

    global VIN
    VIN = 42
    print("Будущее вселенной:", future(1e30, 5e25, G=6.67430e-11, c=299792458))

    print("Сопротивление цепи (последовательно):", circuit_resistance(10, 20, 30))
    print("Сопротивление цепи (параллельно):", circuit_resistance(10, 20, 30, connection='parallel'))
    print("Проводимость цепи (параллельно):", circuit_resistance(10, 20, 30, connection='parallel', conductivity=True))


if __name__ == "__main__":
    main()
