class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self):
        print(f"{self.name} атакует и наносит {self.attack_power} урона!")

    def info(self):
        print(f'Имя: {self.name}')
        print(f'Очки здоровья: {self.hp}')
        print(f'Урон: {self.attack_power}')

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, hp = 200, attack_power = 50)

    def warrior_attack(self):
        print(f'{self.name} атакует и наносит {self.attack_power} урона!')

    def info(self):
        print(f'Имя: {self.name}')
        print(f'Очки здоровья: {self.hp}')
        print(f'Урон: {self.attack_power}')

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, hp = 50, attack_power = 75)
        self.mana = 100

    def mage_attack(self):
        if self.mana >= 10:
            print(f'{self.name} атакует магией и наносит {self.attack_power} урона!')
            self.mana -= 10
        else:
            print('Not enough mana!')

    def info(self):
        print(f'Имя: {self.name}')
        print(f'Очки здоровья: {self.hp}')
        print(f'Урон: {self.attack_power}')
        print(f'Мана: {self.mana}')

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, hp=125, attack_power=14)
        self.arrows = 10

    def attack(self):
        if self.arrows > 0:
            print(f"{self.name} выпускает стрелу и наносит {self.attack_power} урона!")
            self.arrows -= 1
        else:
            print(f"У лучника {self.name} закончились стрелы!")

    def info(self):
        super().info()
        print(f"Стрелы: {self.arrows}")







