def generate_sentence(subjects, verbs, objects):
    for subject, verb, object in zip(subjects, verbs, objects):
        yield " ".join((subject, verb, object))
