from statistics import mean
from task_4 import *

DEFAULT_BOOK = r"recipes/small-db.json"
TEST_DB_PATH = "recipes/test-db.json"
LARGE_DATA_DB_PATH = "recipes/20170107-061401-recipeitems.json"


def test_search_empty_filters():
    assert any(search(file_name=TEST_DB_PATH))


def test_search_no_results():
    keywords = ["pp"]
    assert not any(search(file_name=TEST_DB_PATH, keywords=keywords))

    keywords = ["aa", "pp"]
    assert not any(search(file_name=TEST_DB_PATH, keywords=keywords))

    keywords = ["aa"]
    ingredients_to_exclude = ["one", "two"]
    assert not any(
        search(file_name=TEST_DB_PATH, keywords=keywords, ingredients_to_exclude=ingredients_to_exclude))

    keywords = ["aa", "First"]
    ingredients_to_include = ["nine"]
    assert not any(
        search(file_name=TEST_DB_PATH, keywords=keywords, ingredients_to_include=ingredients_to_include))


def test_search_sanity():
    keywords = ["ver", "yummy"]
    ingredients_to_include = ["two", "2"]
    output = search(keywords=keywords, ingredients_to_include=ingredients_to_include, file_name=TEST_DB_PATH)

    output = list(output)
    assert len(output) == 2
    assert output[0]["name"] == "First name"
    assert output[1]["name"] == "Third name"

    keywords = ["yummy"]
    ingredients_to_include = ["one", "1"]
    output = search(file_name=TEST_DB_PATH, keywords=keywords, ingredients_to_include=ingredients_to_include)

    output = list(output)
    assert len(output) == 1
    assert output[0]["name"] == "First name"

    keywords = ["yummy"]
    ingredients_to_include = ["two", "2"]
    ingredients_to_exclude = ["one", "1"]
    output = search(file_name=TEST_DB_PATH, keywords=keywords, ingredients_to_include=ingredients_to_include,
                    ingredients_to_exclude=ingredients_to_exclude)

    output = list(output)
    assert len(output) == 1
    assert output[0]["name"] == "Third name"

    keywords = ["yummy"]
    ingredients_to_exclude = ["one"]
    output = search(file_name=TEST_DB_PATH, keywords=keywords, ingredients_to_exclude=ingredients_to_exclude)

    output = list(output)
    assert len(output) == 1
    assert output[0]["name"] == "Third name"


def test_search_large_data():
    output = search(file_name=LARGE_DATA_DB_PATH)
    assert next(output)


def test_search_large_data2():
    output = search(keywords=["Dinner"], file_name=LARGE_DATA_DB_PATH)
    assert next(output)


def test_two_searches_in_parallel():
    output1 = search(file_name=TEST_DB_PATH)
    output2 = search(file_name=TEST_DB_PATH)
    next(output1)
    next(output2)

    assert next(output1)["name"] == "Second name"
    assert next(output2)["name"] == "Second name"


# function can be: average, count, max, min, sum
def test_statistics_average():
    assert statistics(mean, "recipeYield", _get_test_recipe_book()) == (8 + 8 + 12) / 3


def test_statistics_max():
    assert statistics(max, "recipeYield", _get_test_recipe_book()) == 12


def test_statistics_min():
    assert statistics(min, "recipeYield", _get_test_recipe_book()) == 8


def test_statistics_sum():
    assert statistics(sum, "recipeYield", _get_test_recipe_book()) == 8 + 8 + 12


def test_statistics_count():
    raise NotImplementedError


def _get_test_recipe_book():
    recipe_book = []

    with open("recipes/test-db.json") as f:
        for line in f:
            recipe_book.append(json.loads(line))

    return recipe_book
