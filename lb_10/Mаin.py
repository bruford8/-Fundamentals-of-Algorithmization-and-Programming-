def craft_item(item):
    inventory = {}
    for material, amount in item._materials_bought:
        inventory[material] = inventory.get(material, 0) + amount

    for material, needed_amount in item._required_materials.items():
        if inventory.get(material, 0) < needed_amount:
            print("Error: You haven't bought the required materials yet")
            return

    item._status = True

    new_materials_bought = []
    used_materials = item._required_materials.copy()

    for material, amount in item._materials_bought:
        if material in used_materials and used_materials[material] > 0:
            if amount <= used_materials[material]:
                used_materials[material] -= amount
            else:
                new_materials_bought.append((material, amount - used_materials[material]))
                used_materials[material] = 0
        else:
            new_materials_bought.append((material, amount))

    item._materials_bought = new_materials_bought
    print('The item was successfully crafted')


from main import Reforged_sword_of_Pan_Radzig, Broad_longsword, Witcher_Silver_Sword

a = Reforged_sword_of_Pan_Radzig()
b = Broad_longsword()
c = Witcher_Silver_Sword()

a.buy('Toledo steel', 3)
craft_item(a)
a.info()
