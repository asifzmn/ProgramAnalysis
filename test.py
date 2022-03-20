def test():
    if True:
        return 1
    return 5


def test2():
    if True:
        return 5
    return 5


def truth():
    return True


def test3():
    if truth():
        return 5
    return 5
