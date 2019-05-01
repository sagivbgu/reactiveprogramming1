from statistics import mean

import pytest

from task_4 import *

DEFAULT_BOOK = r"recipes/small-db.json"
TEST_DB_PATH = "recipes/test-db.json"
LARGE_DATA_DB_PATH = "recipes/20170107-061401-recipeitems.json"


# def test_search_no_args():
#    with pytest.raises(ValueError):
#        search(TEST_DB_PATH)


def test_search_no_results():
    assert not any(search(TEST_DB_PATH, "pp"))
    assert not any(search(TEST_DB_PATH, "aa", "pp"))
    assert not any(search(TEST_DB_PATH, "aa", "-one", "-two"))
    assert not any(search(TEST_DB_PATH, "aa", "First", "+nine"))


def test_search_sanity():
    output = search(TEST_DB_PATH, "ver", "yummy", "+two", "+2")
    output = list(output)
    assert len(output) == 2
    assert output[0]["name"] == "First name"
    assert output[1]["name"] == "Third name"

    output = search(TEST_DB_PATH, "yummy", "+one", "+1")
    output = list(output)
    assert len(output) == 1
    assert output[0]["name"] == "First name"

    output = search(TEST_DB_PATH, "yummy", "+two", "+2", "-one", "-1")
    output = list(output)
    assert len(output) == 1
    assert output[0]["name"] == "Third name"

    output = search(TEST_DB_PATH, "yummy", "-one")
    output = list(output)
    assert len(output) == 1
    assert output[0]["name"] == "Third name"


def test_search_large_data():
    output = search(LARGE_DATA_DB_PATH, "")
    assert next(output)


def test_search_large_data2():
    output = search(LARGE_DATA_DB_PATH, "Dinner")
    assert next(output)


def test_two_searches_in_parallel():
    output1 = search(TEST_DB_PATH, "")
    output2 = search(TEST_DB_PATH, "")
    next(output1)
    next(output2)

    assert next(output1)["name"] == "Second name"
    assert next(output2)["name"] == "Second name"


# function can be: average, count, max, min, sum
def test_statistics_average():
    def average(data):
        data = [int(d) for d in data]
        return mean(data)

    assert statistics(aggregate_function=average, data=_get_test_recipe_book(), property="recipeYield") == (
            8 + 8 + 12) / 3


def test_statistics_max():
    def maximum(data):
        data = [int(d) for d in data]
        return max(data)

    assert statistics(aggregate_function=maximum, data=_get_test_recipe_book(), property="recipeYield") == 12


def test_statistics_count():
    assert statistics(lambda d: len(list(d)), data=_get_test_recipe_book()) == 3


def _get_test_recipe_book():
    recipe_book = []

    with open("recipes/test-db.json") as f:
        for line in f:
            recipe_book.append(json.loads(line))

    return recipe_book
