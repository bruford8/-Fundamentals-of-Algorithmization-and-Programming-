class Tamagochi:
    def __init__(self, name, hp, hunger, sleep_hours):
        self.name = name
        self.hp = hp
        self.hunger = hunger
        self.sleep_hours = sleep_hours

    def info(self):
        print(f'У {self.name} {self.hp} очков здоровья!')
        print(f'У {self.name} {self.hunger} очков голода!')
        print(f'У {self.name} {self.sleep_hours} очков сна!')

    def check_status(self):
        if self.hunger <= 0:
            print(f'{self.name} умер от голода...')
            return False
        elif self.sleep_hours < 0:
            print(f'{self.name} умер от недосыпа...')
            return False
        print('Все хорошо!')
        return True

    def feed(self):
        if not self.check_status():
            return
        print(f'Вы покормили {self.name}!')
        self.hunger += 75
        print(f'Голод: {self.hunger}')

    def play(self):
        if not self.check_status():
            return
        print(f'Вы играете с {self.name}, и весело проводите время!')
        self.hunger -= 5
        self.sleep_hours -= 10

    def sleep(self):
        if not self.check_status():
            return
        print(f'{self.name} спит!')
        self.sleep_hours += 100
        self.hunger -= 5
        self.stress -= 15




