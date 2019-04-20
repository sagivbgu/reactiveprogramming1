from types import GeneratorType

from task_3 import *


def test_generate_n_grams():
    sentence = "the quick red fox jumps over the lazy brown dog"

    assert type(generate_n_grams(3, sentence)) == GeneratorType

    expected_lists = (
        ["the", "quick", "red"],
        ["quick", "red", "fox"],
        ["red", "fox", "jumps"],
        ["fox", "jumps", "over"],
        ["jumps", "over", "the"],
        ["over", "the", "lazy"],
        ["the", "lazy", "brown"],
        ["lazy", "brown", "dog"]
    )

    assert tuple(generate_n_grams(3, sentence)) == expected_lists


def test_generate_n_grams_size_exceeds():
    sentence = "the quick red fox jumps over the lazy brown dog"
    assert tuple(generate_n_grams(100, sentence)) == ()


def test_generate_sentence():
    sentences = generate_sentence(["I", "You"], ["play", "love"], ["Basketball", "Football"])
    expected_sentences = ["I play Basketball", "You love Football"]
    for sentence, expected_sentence in zip(sentences, expected_sentences):
        assert sentence == expected_sentence


def test_generate_permutations_example1():
    some_list = [1, 2]
    expected_permutations = (
        (1, 2),
        (2, 1)
    )

    assert tuple(generate_permutations(some_list)) == expected_permutations


def test_generate_permutations_example2():
    some_list = [1, 'a', True]
    expected_permutations = (
        (1, 'a', True),
        (1, True, 'a'),
        ('a', 1, True),
        ('a', True, 1),
        (True, 1, 'a'),
        (True, 'a', 1)
    )

    assert tuple(generate_permutations(some_list)) == expected_permutations


def test_generate_permutations_empty_list():
    assert tuple(generate_permutations([])) == ()
