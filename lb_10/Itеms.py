class Reforged_sword_of_Pan_Radzig:
    def __init__(self):
        self._name = "Reforged_sword_of_Pan_Radzig"
        self._status = False
        self._titanite_fragments = 0
        self._materials = {'Toledo steel': 0}
        self._materials_bought = []
        self._required_materials = {'Toledo steel': 3}

    def _add_material(self, material_name, amount):
        if material_name in self._materials:
            self._materials[material_name] += amount
        else:
            raise AttributeError

    def _add_titanite(self, amount):
        self._titanite_fragments += amount

    def info(self):
        if self._status:
            print('Strength: 20\nDefence: 299\nWeight: 1.9\nAgility: 23\nDurability: 240\n'
                  'Price: ??\nStab damage: 199\nSlash damage: 190\nBlunt damage: 38\n')
        else:
            print("You don't have this item")

    def upgrade(self, a):
        if self._status and 0 < a <= 5:
            if a > self._titanite_fragments:
                print('Not enough titanite')
            else:
                self._titanite_fragments -= a
                print(f'{self._name} +{a}')
                print(f'Strength: {20 + a * 20}\nDefence: {299 + a * 20}\nWeight: {1.9 + a * 20}\n'
                      f'Agility: {23 + a * 20}\nDurability: {240 + a * 20}\nPrice: ??\n'
                      f'Stab damage: {199 + a * 20}\nSlash damage: {190 + a * 20}\nBlunt damage: {38 + a * 20}')
        else:
            print('Not upgraded')

    def disassembly(self):
        if self._status:
            print(f'You are disassembling {self._name}')
            self._materials['Toledo steel'] += 3
            self._status = False
        else:
            print('You have nothing to disassemble')

    def buy(self, material_name, amount):
        try:
            self._add_material(material_name, amount)
            self._materials_bought.append((material_name, amount))
            print(f'You have bought {amount} of {material_name}')
        except AttributeError:
            print('Error: Cannot add material to this item')

    def buy_titanite_fragments(self, amount):
        self._add_titanite(amount)
        print(f'You have bought {amount} Titanite fragments')


class Broad_longsword:
    def __init__(self):
        self._name = "Broad_longsword"
        self._status = False
        self._titanite_fragments = 0
        self._materials = {
            'Cow skin': 0,
            'Pear sword Pommel': 0,
            'Ordinary sword guard': 0,
            'Frankfurt steel': 0,
            'Iron': 0
        }
        self._materials_bought = []
        self._required_materials = {
            'Cow skin': 1,
            'Pear sword Pommel': 1,
            'Ordinary sword guard': 1,
            'Frankfurt steel': 3,
            'Iron': 2
        }

    def _add_material(self, material_name, amount):
        if material_name in self._materials:
            self._materials[material_name] += amount
        else:
            raise AttributeError

    def _add_titanite(self, amount):
        self._titanite_fragments += amount

    def info(self):
        if self._status:
            print('Strength: 16\nDefence: 246\nWeight: 2.9\nAgility: 19\nDurability: 200\n'
                  'Price: ??\nStab damage: 166\nSlash damage: 158\nBlunt damage: 32\n')
        else:
            print("You don't have this item")

    def upgrade(self, a):
        if self._status and 0 < a <= 5:
            if a > self._titanite_fragments:
                print('Not enough titanite')
            else:
                self._titanite_fragments -= a
                print(f'{self._name} +{a}')
                print(f'Strength: {16 + a * 20}\nDefence: {246 + a * 20}\nWeight: {2.9 + a * 20}\n'
                      f'Agility: {19 + a * 20}\nDurability: {200 + a * 20}\nPrice: ??\n'
                      f'Stab damage: {166 + a * 20}\nSlash damage: {158 + a * 20}\nBlunt damage: {32 + a * 20}')
        else:
            print('Not upgraded')

    def disassembly(self):
        if self._status:
            print(f'You are disassembling {self._name}')
            for mat, count in self._required_materials.items():
                self._materials[mat] += count
            self._status = False
        else:
            print('You have nothing to disassemble')

    def buy(self, material_name, amount):
        try:
            self._add_material(material_name, amount)
            self._materials_bought.append((material_name, amount))
            print(f'You have bought {amount} of {material_name}')
        except AttributeError:
            print('Error: Cannot add material to this item')

    def buy_titanite_fragments(self, amount):
        self._add_titanite(amount)
        print(f'You have bought {amount} Titanite fragments')


class Witcher_Silver_Sword:
    def __init__(self):
        self._name = "Witcher_Silver_Sword"
        self._status = False
        self._titanite_fragments = 0
        self._materials = {
            'Diamond Dust': 0,
            'A piece of wood': 0,
            'Iron ore': 0,
            'Silver ore': 0
        }
        self._materials_bought = []
        self._required_materials = {
            'Diamond Dust': 1,
            'A piece of wood': 1,
            'Iron ore': 1,
            'Silver ore': 3
        }

    def _add_material(self, material_name, amount):
        if material_name in self._materials:
            self._materials[material_name] += amount
        else:
            raise AttributeError

    def _add_titanite(self, amount):
        self._titanite_fragments += amount

    def info(self):
        if self._status:
            print('Damage: 10-17\nBleeding: +7%\nWeight: 16')
        else:
            print("You don't have this item")

    def upgrade(self, a):
        if self._status and 0 < a <= 5:
            if a > self._titanite_fragments:
                print('Not enough titanite')
            else:
                self._titanite_fragments -= a
                print(f'{self._name} +{a}')
                print(f'Damage: {10 + a * 2}-{17 + a * 3}\nBleeding: +{7 + a * 2}%\nWeight: 16\nPrice: ??')
        else:
            print('Not upgraded')

    def disassembly(self):
        if self._status:
            print(f'You are disassembling {self._name}')
            for mat, count in self._required_materials.items():
                self._materials[mat] += count
            self._status = False
        else:
            print('You have nothing to disassemble')

    def buy(self, material_name, amount):
        try:
            self._add_material(material_name, amount)
            self._materials_bought.append((material_name, amount))
            print(f'You have bought {amount} of {material_name}')
        except AttributeError:
            print('Error: Cannot add material to this item')

    def buy_titanite_fragments(self, amount):
        self._add_titanite(amount)
        print(f'You have bought {amount} Titanite fragments')





