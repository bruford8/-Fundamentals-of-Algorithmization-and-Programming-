def groundhog_day(strings):
    if not strings or any(len(s) != len(strings[0]) for s in strings):
        return (0, 0)

    for i in range(1, len(strings)):
        differences = [j for j in range(len(strings[i])) if strings[i][j] != strings[i - 1][j]]
        if len(differences) > 2:
            return (i, differences)

    return (0, 0)
data = [
    "Groundhog day festivities in punxsutawney",
    "Groundhog day festivities in punxsutawney",
    "Groundhog day festivities in punxsutawney",
    "Groundhog day festivities in punxsutawney"
]
result = groundhog_day(data)
