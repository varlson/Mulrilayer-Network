def terminal_clear():
    import sys
    from importlib import reload
    sys.modules[__name__].__dict__.clear()

def gen(s):

    from random import randint, shuffle
    return [randint(1, 67) for x in range(s)]



def show(mob, sorte, g):

    for index, node in enumerate(sorte):
        print(mob[index]+'--- '+g.vs['label'][node[0]])


def show(mob, g):
    for m in mob:
        print(m in g.vs['label'])