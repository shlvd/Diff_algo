def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])

def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])

def max(list):
    if list == []:
        return None
    if len(list) == 1:
        return list[0]
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    return list[0] if list[0] > max(list[1:]) else max(list[1:])

