def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    return max(lst[0], find_max(lst[1:]))