from task_3 import *


def test_generate_sentence():
    sentences = generate_sentence(["I", "You"], ["play", "love"], ["Basketball", "Football"])
    expected_sentences = ["I play Basketball", "You love Football"]
    for sentence, expected_sentence in zip(sentences, expected_sentences):
        assert sentence == expected_sentence
