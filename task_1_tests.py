from task_1 import *


def test_p_2_lc():
    assert p_2_lc([3, 5, 9, 8]) == [True, False, True, False]


def test_p_2_fo():
    assert p_2_fo([3, 5, 9, 8]) == [True, False, True, False]


def test_p_4_lc():
    assert p_4_lc(["apple", "orange", "pear"]) == ["A", "O", "P"]


def test_p_4_fo():
    assert p_4_fo(["apple", "orange", "pear"]) == ["A", "O", "P"]


def test_p_6_lc():
    assert p_6_lc(["apple", "orange", "pear"]) == [("apple", 5), ("orange", 6), ("pear", 4)]


def test_p_6_fo():
    assert p_6_fo(["apple", "orange", "pear"]) == [("apple", 5), ("orange", 6), ("pear", 4)]


def test_p_8_lc():
    assert p_8_lc([1, 2, 4, 5, 7]) == [1, 4, 7]


def test_p_8_fo():
    assert p_8_fo([1, 2, 4, 5, 7]) == [1, 4, 7]
