def p_1_lc(inputlist):
    return [2 * x + 1 for x in inputlist]


def p_1_fo(inputlist):
    return list(map(lambda x: 2 * x + 1, inputlist))


def p_2_lc(inputlist):
    return [x % 3 == 0 for x in inputlist]


def p_2_fo(inputlist):
    return list(map(lambda x: x % 3 == 0, inputlist))


def p_3_lc(inputlist):
    return [num ** 2 for num in inputlist]


def p_3_fo(inputlist):
    return list(map(lambda num: num ** 2, inputlist))


def p_4_lc(inputlist):
    return [x[0].upper() for x in inputlist]


def p_4_fo(inputlist):
    return list(map(lambda x: x[0].upper(), inputlist))


def p_5_lc(inputlist):
    return [word for word in inputlist if "p" in word]


def p_5_fo(inputlist):
    return list(filter(lambda word: "p" in word, inputlist))


def p_6_lc(inputlist):
    return [(x, len(x)) for x in inputlist]


def p_6_fo(inputlist):
    return list(map(lambda x: (x, len(x)), inputlist))


def p_7_lc(inputlist):
    return [num for num in inputlist if num % 2 != 0]


def p_7_fo(inputlist):
    return list(filter(lambda num: num % 2 != 0, inputlist))


def p_8_lc(inputlist):
    return inputlist[::2]  # TODO: Ask Majeed since it's not a list comprehension
                           # CR: I'd change it to a regular list comprehension


# TODO: Is there a smarter way?
def p_8_fo(inputlist):
                                 # CR: Maybe change the lambda to - lambda i, x: i % 2 == 0?
    enumerable_at_even_indexes = filter(lambda x: x[0] % 2 == 0, enumerate(inputlist))
                    # CR: Same here - lambda i, x: x
    return list(map(lambda x: x[1], enumerable_at_even_indexes))
