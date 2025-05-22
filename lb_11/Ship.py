class Ship:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.status = True

    def info(self):
        print(f'Название корабля: {self.name}\n'
              f'Состояние: {self.hp} квадрата')


class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def attack(self):
        pass

    def info(self):
        print(f'Имя: {self.name}\n'
              f'Цвет команды: {self.color}')


class Playing_field:
    def __init__(self, name, height, width):
        self.name = name
        self.height = height
        self.width = width

    def clear(self):
        pass

    def info(self):
        print(f'Название карты: {self.name}\n'
              f'Размер карты: {self.height * self.width} px')


playing_field = Playing_field('Море', 10, 10)
aircraft_carrier4_1 = Ship('Авианосец', 4)
battleship3_1 = Ship('Линкор', 3)
battleship3_2 = Ship('Линкор_2', 3)
cruiser2_1 = Ship('Крейсер', 2)
cruiser2_2 = Ship('Крейсер_2', 2)
cruiser2_3 = Ship('Крейсер_3', 2)
the_destroyer1_1 = Ship('Эсминец', 1)
the_destroyer1_2 = Ship('Эсминец', 1)
the_destroyer1_3 = Ship('Эсминец', 1)
the_destroyer1_4 = Ship('Эсминец', 1)
aircraft_carrier4_1.info()
playing_field.info()
player1 = Player('Игрок_1', 'Red')
player2 = Player('Игрок_2', 'Blue')
player1.info()
