class Ship:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.status = True


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
