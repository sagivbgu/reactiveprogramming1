from task_1 import *


def test_p_1():
    inputlist, expected_list = [0, 1, 2, 3], [1, 3, 5, 7]
    assert p_1_lc(inputlist) == expected_list
    assert p_1_fo(inputlist) == expected_list


def test_p_2_lc():
    assert p_2_lc([3, 5, 9, 8]) == [True, False, True, False]


def test_p_2_fo():
    assert p_2_fo([3, 5, 9, 8]) == [True, False, True, False]


def test_p_3():
    inputlist, expected_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    assert p_3_lc(inputlist) == expected_list
    assert p_3_fo(inputlist) == expected_list


def test_p_4_lc():
    assert p_4_lc(["apple", "orange", "pear"]) == ["A", "O", "P"]


def test_p_4_fo():
    assert p_4_fo(["apple", "orange", "pear"]) == ["A", "O", "P"]


def test_p_5():
    inputlist, expected_list = ["apple", "orange", "pear"], ["apple", "pear"]
    assert p_5_lc(inputlist) == expected_list
    assert p_5_fo(inputlist) == expected_list


def test_p_6_lc():
    assert p_6_lc(["apple", "orange", "pear"]) == [("apple", 5), ("orange", 6), ("pear", 4)]


def test_p_6_fo():
    assert p_6_fo(["apple", "orange", "pear"]) == [("apple", 5), ("orange", 6), ("pear", 4)]


def test_p_7():
    inputlist, expected_list = [0, 1, 2, 3, 4, 5, 6, 8], [1, 3, 5]
    assert p_7_lc(inputlist) == expected_list
    assert p_7_fo(inputlist) == expected_list


def test_p_8_lc():
    assert p_8_lc([1, 2, 4, 5, 7]) == [1, 4, 7]


def test_p_8_fo():
    assert p_8_fo([1, 2, 4, 5, 7]) == [1, 4, 7]
