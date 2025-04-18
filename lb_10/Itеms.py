class Reforged_sword_of_Pan_Radzig:
    def __init__(self):
        self.__name = "Reforged_sword_of_Pan_Radzig"
        self.__status = False
        self.__toledo_steel = 0
        self.__titanite_fragments = 0

    def _add_material(self, material_name, amount):
        if material_name == 'Toledo steel':
            self.__toledo_steel += amount
        else:
            raise AttributeError

    def _add_titanite(self, amount):
        self.__titanite_fragments += amount

    def craft(self):
        if self.__toledo_steel >= 3:
            self.__status = True
            self.__toledo_steel -= 3
            print('The item was successfully crafted')
        else:
            print('Error. Not enough item')

    def info(self):
        if self.__status:
            print('Strength: 20\nDefence: 299\nWeight: 1.9\nAgility: 23\nDurability: 240\n'
                  'Price: ??\nStab damage: 199\nSlash damage: 190\nBlunt damage: 38\n')
        else:
            print("You don't have this item")

    def upgrade(self, a):
        if self.__status and 0 < a <= 5:
            if a > self.__titanite_fragments:
                print('Not enough titanite')
            else:
                self.__titanite_fragments -= a
                print(f'Reforged_sword_of_Pan_Radzig +{a}')
                print(f'Strength: {20 + a * 20}\nDefence: {299 + a * 20}\nWeight: {1.9 + a * 20}\n'
                      f'Agility: {23 + a * 20}\nDurability: {240 + a * 20}\nPrice: ??\n'
                      f'Stab damage: {199 + a * 20}\nSlash damage: {190 + a * 20}\nBlunt damage: {38 + a * 20}')
        else:
            print('Not upgraded')

    def disassembly(self):
        if self.__status:
            print('You are disassembling Reforged_sword_of_Pan_Radzig')
            self.__toledo_steel += 3
            self.__status = False
        else:
            print('You have nothing to disassemble')


class Broad_longsword:
    def __init__(self):
        self.__status = False
        self.__titanite_fragments = 0
        self.__cow_skin = 0
        self.__pear_sword_pommel = 0
        self.__ordinary_sword_guard = 0
        self.__frankfurt_steel = 0
        self.__iron = 0

    def _add_material(self, material_name, amount):
        match material_name:
            case 'Cow skin':
                self.__cow_skin += amount
            case 'Pear sword Pommel':
                self.__pear_sword_pommel += amount
            case 'Ordinary sword guard':
                self.__ordinary_sword_guard += amount
            case 'Frankfurt steel':
                self.__frankfurt_steel += amount
            case 'Iron':
                self.__iron += amount
            case _:
                raise AttributeError

    def _add_titanite(self, amount):
        self.__titanite_fragments += amount

    def craft(self):
        if (self.__cow_skin >= 1 and self.__pear_sword_pommel >= 1 and
                self.__ordinary_sword_guard >= 1 and self.__frankfurt_steel >= 3 and
                self.__iron >= 2):
            self.__status = True
            self.__cow_skin -= 1
            self.__pear_sword_pommel -= 1
            self.__ordinary_sword_guard -= 1
            self.__frankfurt_steel -= 3
            self.__iron -= 2
            print('The item was successfully crafted')
        else:
            print('Error. Not enough item')

    def info(self):
        if self.__status:
            print('Strength: 16\nDefence: 246\nWeight: 2.9\nAgility: 19\nDurability: 200\n'
                  'Price: ??\nStab damage: 166\nSlash damage: 158\nBlunt damage: 32\n')
        else:
            print("You don't have this item")

    def upgrade(self, a):
        if self.__status and 0 < a <= 5:
            if a > self.__titanite_fragments:
                print('Not enough titanite')
            else:
                self.__titanite_fragments -= a
                print(f'Broad_longsword +{a}')
                print(f'Strength: {16 + a * 20}\nDefence: {246 + a * 20}\nWeight: {2.9 + a * 20}\n'
                      f'Agility: {19 + a * 20}\nDurability: {200 + a * 20}\nPrice: ??\n'
                      f'Stab damage: {166 + a * 20}\nSlash damage: {158 + a * 20}\nBlunt damage: {32 + a * 20}')
        else:
            print('Not upgraded')

    def disassembly(self):
        if self.__status:
            print('You are disassembling Broad_longsword')
            self.__cow_skin += 1
            self.__pear_sword_pommel += 1
            self.__ordinary_sword_guard += 1
            self.__frankfurt_steel += 3
            self.__iron += 2
            self.__status = False
        else:
            print('You have nothing to disassemble')


class Witcher_Silver_Sword:
    def __init__(self):
        self.__status = False
        self.__titanite_fragments = 0
        self.__diamond_dust = 0
        self.__wood = 0
        self.__iron_ore = 0
        self.__silver_ore = 0

    def _add_material(self, material_name, amount):
        match material_name:
            case 'Diamond Dust':
                self.__diamond_dust += amount
            case 'A piece of wood':
                self.__wood += amount
            case 'Iron ore':
                self.__iron_ore += amount
            case 'Silver ore':
                self.__silver_ore += amount
            case _:
                raise AttributeError

    def _add_titanite(self, amount):
        self.__titanite_fragments += amount

    def craft(self):
        if (self.__diamond_dust >= 1 and self.__wood >= 1 and
                self.__iron_ore >= 1 and self.__silver_ore >= 3):
            self.__status = True
            self.__diamond_dust -= 1
            self.__wood -= 1
            self.__iron_ore -= 1
            self.__silver_ore -= 3
            print('Item was successfully crafted')
        else:
            print('Error. Not enough item')

    def info(self):
        if self.__status:
            print('Damage: 10-17\nBleeding: +7%\nWeight: 16')
        else:
            print("You don't have this item")

    def upgrade(self, a):
        if self.__status and 0 < a <= 5:
            if a > self.__titanite_fragments:
                print('Not enough titanite')
            else:
                self.__titanite_fragments -= a
                print(f'Witcher_Silver_Sword +{a}')
                print(f'Damage: {10 + a * 2}-{17 + a * 3}\nBleeding: +{7 + a * 2}%\nWeight: 16\nPrice: ??')
        else:
            print('Not upgraded')

    def disassembly(self):
        if self.__status:
            print('You are disassembling Witcher_Silver_Sword')
            self.__diamond_dust += 1
            self.__wood += 1
            self.__iron_ore += 1
            self.__silver_ore += 3
            self.__status = False
        else:
            print('You have nothing to disassemble')


def buy(self, material_name, amount):
    try:
        self._add_material(material_name, amount)
        print(f'You have bought {amount} of {material_name}')
    except AttributeError:
        print('Error: Cannot add material to this item')


def buy_titanite_fragments(self, amount):
    try:
        self._add_titanite(amount)
        print(f'You have bought {amount} Titanite fragments')
    except AttributeError:
        print('Error: Cannot add titanite to this item')
