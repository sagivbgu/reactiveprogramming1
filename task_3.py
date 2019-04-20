def generate_n_grams(size, words_list):
    words = words_list.split(" ")
    for i in range(len(words) - size + 1):
        yield words[i:i + size]


def generate_sentence(subjects, verbs, objects):
    for subject, verb, obj in zip(subjects, verbs, objects):
        yield " ".join((subject, verb, obj))


def generate_permutations(some_list):
    if len(some_list) == 1:
        yield tuple(some_list[0])

    elif len(some_list) == 2:
        yield (some_list[0], some_list[1])
        yield (some_list[1], some_list[0])

    else:
        for i in range(len(some_list)):
            new_list = some_list[:]
            new_list.pop(i)
            for inner_perm in generate_permutations(new_list):
                yield (some_list[i],) + inner_perm
