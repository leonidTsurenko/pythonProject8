result = []

def divider(a: object, b: object) -> object:
    """

    :rtype: object
    """
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a/b

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}

for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)
if int == type(key):
    pass
else:
    raise
