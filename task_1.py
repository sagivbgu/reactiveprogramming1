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
    return [x[0].upper() if x else "" for x in inputlist]


def p_4_fo(inputlist):
    return list(map(lambda x: x[0].upper() if x else "", inputlist))


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
    return inputlist[::2]


def p_8_fo(inputlist):
    even_indexes = range(0, len(inputlist), 2)
    return list(map(lambda i: inputlist[i], even_indexes))
