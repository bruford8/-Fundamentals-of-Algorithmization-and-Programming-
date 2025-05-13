class Ship:
    def __init__(self):
        self.size = 5
        self.hp = 5
        self.status = True

    pass

class Battleship(Ship):
    def __init__(self):
        super().__init__()
        self.size = 10
        self.hp = 10
        self.status = True

    pass

class Cruiser(Ship):
    def __init__(self):
        super().__init__()
        self.size = 8
        self.hp = 8
        self.status = True

    pass

class TheDestroyer(Ship):
    def __init__(self):
        super().__init__()
        self.size = 6
        self.hp = 6
        self.status = True

    pass

class Boat(Ship):
    def __init__(self):
        super().__init__()
        self.size = 3
        self.hp = 3
        self.status = True

    pass

class Player1:
    def __init__(self, name):
        self.name = name

    def fire(self):

class Player2:
    def __init__(self, name):
        self.name = name

    def fire(self):

