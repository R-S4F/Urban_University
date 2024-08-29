sides = (2,3,5)
__SIDES_COUNT = 3

def qwerty(sides, __SIDES_COUNT):
    if len(sides) == __SIDES_COUNT:
        for i in [*sides]:
            if not (i > 0 and isinstance(i, int)):
                return False
        return True
    else:
        return False
print(qwerty(sides,__SIDES_COUNT))