def quarters(*points):
    result = {1: 0, 2: 0, 3: 0, 4: 0}
    for x, y in points:
        if x > 0 and y > 0:
            result[1] += 1
        elif x < 0 and y > 0:
            result[2] += 1
        elif x < 0 and y < 0:
            result[3] += 1
        elif x > 0 and y < 0:
            result[4] += 1
    return result
