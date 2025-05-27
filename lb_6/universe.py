VIN = 42


def future(*masses, **constants):
    total_mass = sum(masses)
    total_constants = sum(constants.values())
    universe_value = total_mass * total_constants

    if universe_value > VIN:
        return "ACCELERATION"
    elif universe_value < VIN:
        return "DECELERATION"
    else:
        return "UNCHANGED"
