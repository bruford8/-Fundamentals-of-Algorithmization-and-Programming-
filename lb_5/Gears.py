def gears(gear_lists, n, m):
    target_ratio = n / m

    gear_set = set()

    for gear_list in gear_lists:
        for gear in gear_list:
            if gear != 0:
                required_gear = target_ratio * gear
                if required_gear in gear_set:
                    return (gear, required_gear)
            gear_set.add(gear)
    return (None, None)
gear_lists = [[0, 2, 30,15], [14, 3, 21, 60], [7, 16, 24, 8]]
n = 7
m = 30
result = gears(gear_lists, n, m)