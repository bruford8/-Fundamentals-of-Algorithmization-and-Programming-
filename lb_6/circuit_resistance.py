def circuit_resistance(*resistances, connection='serial', conductivity=False):
    if connection == 'serial':
        total = sum(resistances)
    elif connection == 'parallel':
        total = 1 / sum(1 / r for r in resistances)
    else:
        raise ValueError("Unknown connection type")

    if conductivity:
        result = 1 / total
    else:
        result = total
    return round(result, 4)

