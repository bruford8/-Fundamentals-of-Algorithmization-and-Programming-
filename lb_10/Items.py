class Reforged_sword_of_Pan_Radzig:
    def __init__(self):
        self.name = Reforged_sword_of_Pan_Radzig
        self.status = False
        self.Toledo_steal = 0
        self.Titanite_fragments = 0

    def buy(self, name, a):
        self.name = name
        if name == 'Toledo steel':
            self.Toledo_steal += a
        else:
            print('Error')

    def craft(self):
        if self.Toledo_steal >= 3:
            self.status = True
            self.Toledo_steal -= 3
            print('The item was successfully crafted')
        else:
            print('Error. Not enough item')

    def info(self):
        if self.status is True:
            print('Strength: 20 \n'
                  'Defence: 299 \n'
                  'Weight: 1.9 \n'
                  'Agility: 23 \n'
                  'Durability: 240 \n'
                  'Price: ?? \n'
                  'Stab damage: 199 \n'
                  'Slash damage: 190 \n'
                  'Blunt damage: 38 \n')
        else:
            print("You don't have this item")

    def buy_titanite_fragments(self, a):
        print(f'You have bought {a} Titanite fragments')
        self.Titanite_fragments += a

    def upgrade(self, a):
        if self.status is True and a <= 5 and self.Titanite_fragments > 0:
            if a > self.Titanite_fragments:
                print('Not enough titanite')
            else:
                print(f'Reforged_sword_of_Pan_Radzig +', str(a))
                self.Titanite_fragments -= a
                print(f'Strength: {20 + a * 20}\n'
                      f'Defence: {299 + a * 20} \n'
                      f'Weight: {1.9 + a * 20} \n'
                      f'Agility: {23 + a * 20} \n'
                      f'Durability: {240 + a * 20} \n'
                      'Price: ?? \n'
                      f'Stab damage: {199 + a * 20} \n'
                      f'Slash damage: {190 + a * 20} \n'
                      f'Blunt damage: {38 + a * 20} \n')
        else:
            print('Not upgraded')

    def disassembly(self):
        if self.status is True:
            print('You are disassembling Reforged_sword_of_Pan_Radzig')
            self.Toledo_steal += 3
        else:
            print('You have nothing to disassemble')

class Broad_longsword:
    def __init__(self):
        self.Titanite_fragments = 0
        self.name = Broad_longsword
        self.status = False
        self.Cow_skin = 0
        self.Pear_sword_Pommel = 0
        self.Ordinary_sword_guard = 0
        self.Frankfurt_steel = 0
        self.Iron = 0

    def buy(self, name, a):
        self.name = name
        if name == 'Cow skin':
            self.Cow_skin += a
        elif name == 'Pear sword Pommel':
            self.Pear_sword_Pommel += a
        elif name == 'Ordinary sword guard':
            self.Ordinary_sword_guard += a
        elif name == 'Frankfurt steel':
            self.Frankfurt_steel += a
        elif name == 'Iron':
            self.Iron += a
        else:
            print('Error')

    def craft(self):
        if self.Cow_skin >= 1 and self.Pear_sword_Pommel >= 1 and self.Ordinary_sword_guard >= 1 and self.Frankfurt_steel >= 3 and self.Iron >= 2:
            self.status = True
            self.Cow_skin -= 1
            self.Pear_sword_Pommel -= 1
            self.Ordinary_sword_guard -= 1
            self.Frankfurt_steel -= 3
            self.Iron -= 2
            print('The item was successfully crafted')
        else:
            print('Error. Not enough item')

    def info(self):
        if self.status is True:
            print('Strength: 16 \n'
                  'Defence: 246 \n'
                  'Weight: 2.9 \n'
                  'Agility: 19 \n'
                  'Durability: 200 \n'
                  'Price: ?? \n'
                  'Stab damage: 166 \n'
                  'Slash damage: 158 \n'
                  'Blunt damage: 32 \n')
        else:
            print("You don't have this item")

    def buy_titanite_fragments(self, a):
        print(f'You have bought {a} Titanite fragments')
        self.Titanite_fragments += a

    def upgrade(self, a):
        if self.status is True and a <= 5 and self.Titanite_fragments > 0:
            if a > self.Titanite_fragments:
                print('Not enough titanite')
            else:
                print(f'Broad_longsword +' , str(a))
                self.Titanite_fragments -= a
                print(f'Strength: {16 + a * 20}\n'
                    f'Defence: {246 + a * 20} \n'
                    f'Weight: {2.9 + a * 20} \n'
                    f'Agility: {19 + a * 20} \n'
                    f'Durability: {200 + a * 20} \n'
                    'Price: ?? \n'
                    f'Stab damage: {166 + a * 20} \n'
                    f'Slash damage: {158 + a * 20} \n'
                    f'Blunt damage: {32 + a * 20} \n')
        else:
            print('Not upgraded')

    def disassembly(self):
        if self.status is True:
            print('You are disassembling broad longsword')
            self.Cow_skin += 1
            self.Pear_sword_Pommel += 1
            self.Ordinary_sword_guard += 1
            self.Frankfurt_steel += 3
            self.Iron += 2
        else:
            print('You have nothing to disassemble')

class Witcher_Silver_Sword:
    def __init__(self):
        self.status = False
        self.Titanite_fragments = 0
        self.Diamond_Dust = 0
        self.A_piece_of_wood = 0
        self.Iron_ore = 0
        self.Silver_ore = 0

    def buy(self, name, a):
        if name == 'Diamond Dust':
            self.Diamond_Dust += a
        elif name == 'A piece of wood':
            self.A_piece_of_wood += a
        elif name == 'Iron ore':
            self.Iron_ore += a
        elif name == 'Silver ore':
            self.Silver_ore += a
        else:
            print('Error')

    def craft(self):
        if self.Diamond_Dust >= 1 and self.A_piece_of_wood >= 1 and self.Iron_ore >= 1 and self.Silver_ore >= 3:
            self.status = True
            self.Diamond_Dust -= 1
            self.A_piece_of_wood -= 1
            self.Iron_ore -= 1
            self.Silver_ore -= 2
            print('Item was successfully crafted')
        else:
            print('Error. Not enough item')

    def info(self):
        if self.status is True:
            print('Damage: 10-17 \n'
                  'The bleeding: +7% \n'
                  'Weight: 16 \n')
        else:
            print("You don't have this item")

    def buy_titanite_fragments(self, a):
        print(f'You have bought {a} Titanite fragments')
        self.Titanite_fragments += a

    def upgrade(self, a):
        if self.status is True and a <= 5 and self.Titanite_fragments > 0:
            if a > self.Titanite_fragments:
                print('Not enough titanite')
            else:
                print(f'Witcher_Silver_Sword +' , str(a))
                self.Titanite_fragments -= a
                print(f'Damage: {10-17 * a * 20} \n'
                    f'The bleeding: {+7 * a * 20} \n'
                    'Weight: 16 \n'
                    'Price: 16 \n')

    def disassembly(self):
        if self.status is True:
            print('You are disassembling broad longsword')
            self.Diamond_Dust += 1
            self.A_piece_of_wood += 1
            self.Iron_ore += 1
            self.Silver_ore += 2
        else:
            print('You have nothing to disassemble')


