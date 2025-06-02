VIN = 42


def future(*mass, **const):
    total_mass = sum(mass)
    total_constants = sum(const.values())
    universe_value = total_mass * total_constants

    if universe_value > VIN:
        return "ACCELERATION"
    elif universe_value < VIN:
        return "DECELERATION"
    else:
        return "UNCHANGED"
