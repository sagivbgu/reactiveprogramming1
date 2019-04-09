def p_2_lc(inputlist):
    return [x % 3 == 0 for x in inputlist]


def p_2_fo(inputlist):
    return list(map(lambda x: x % 3 == 0, inputlist))


def p_4_lc(inputlist):
    return [x[0].upper() for x in inputlist]


def p_4_fo(inputlist):
    return list(map(lambda x: x[0].upper(), inputlist))


def p_6_lc(inputlist):
    return [(x, len(x)) for x in inputlist]


def p_6_fo(inputlist):
    return list(map(lambda x: (x, len(x)), inputlist))


def p_8_lc(inputlist):
    return inputlist[::2]  # TODO: Ask Majeed since it's not a list comprehension


# TODO: Is there a smarter way?
def p_8_fo(inputlist):
    enumerable_at_even_indexes = filter(lambda x: x[0] % 2 == 0, enumerate(inputlist))
    return list(map(lambda x: x[1], enumerable_at_even_indexes))
