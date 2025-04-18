from items import Reforged_sword_of_Pan_Radzig, Broad_longsword, Witcher_Silver_Sword, buy, buy_titanite_fragments
a = Reforged_sword_of_Pan_Radzig()
b = Broad_longsword()
c = Witcher_Silver_Sword()

buy(b, 'Iron', 10)
buy(b, 'Frankfurt steel', 10)
buy(b, 'Ordinary sword guard', 10)
buy(b, 'Pear sword Pommel', 10)
buy(b, 'Cow skin', 10)
b.craft()
b.info()
buy_titanite_fragments(b, 10)
b.upgrade(5)