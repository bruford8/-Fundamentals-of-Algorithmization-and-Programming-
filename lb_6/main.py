from quarters import quarters
from future import future
from circuit_resistance import circuit_resistance


def main():
    data = [(1, 2), (-1, 3), (4, -2), (-3, -4), (0, 5), (2, 0)]
    for k, v in sorted(quarters(*data).items()):
        print(f'{k}:\t{v}')


    global VIN
    VIN = 42
    mass = [1, 2, 3, 4]
    const = {'charge': 1.6, 'alpha': 0.137, 'pi': 3.14}
    print(future(*mass, **const))


    data = [10, 20, 30]
    print(circuit_resistance(*data))


if __name__ == "__main__":
    main()
