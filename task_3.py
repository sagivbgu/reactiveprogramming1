def generate_sentence(subjects, verbs, objects):
    for subject, verb, obj in zip(subjects, verbs, objects):
        yield " ".join((subject, verb, obj))
