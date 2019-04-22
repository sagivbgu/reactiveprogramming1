from task_4 import *

TEST_DB_PATH = "recipes/test-db.json"
LARGE_DATA_DB_PATH = "recipes/20170107-061401-recipeitems.json"


def test_search_empty_filters():
    assert any(search(recipes_file_path=TEST_DB_PATH))


def test_search_no_results():
    keywords = ["pp"]
    assert not any(search(keywords=keywords, recipes_file_path=TEST_DB_PATH))

    keywords = ["aa"]
    ingredients_to_exclude = ["one"]
    assert not any(
        search(keywords=keywords, ingredients_to_exclude=ingredients_to_exclude, recipes_file_path=TEST_DB_PATH))

    keywords = ["aa"]
    ingredients_to_include = ["nine"]
    assert not any(
        search(keywords=keywords, ingredients_to_include=ingredients_to_include, recipes_file_path=TEST_DB_PATH))


def test_search_sanity():
    keywords = ["yummy"]
    ingredients_to_include = ["two"]
    output = search(keywords=keywords, ingredients_to_include=ingredients_to_include, recipes_file_path=TEST_DB_PATH)

    output = list(output)
    assert len(output) == 2
    assert output[0]["name"] == "First name"
    assert output[1]["name"] == "Third name"

    keywords = ["yummy"]
    ingredients_to_include = ["one"]
    output = search(keywords=keywords, ingredients_to_include=ingredients_to_include, recipes_file_path=TEST_DB_PATH)

    output = list(output)
    assert len(output) == 1
    assert output[0]["name"] == "First name"

    keywords = ["yummy"]
    ingredients_to_include = ["two"]
    ingredients_to_exclude = ["one"]
    output = search(keywords=keywords, ingredients_to_include=ingredients_to_include,
                    ingredients_to_exclude=ingredients_to_exclude, recipes_file_path=TEST_DB_PATH)

    output = list(output)
    assert len(output) == 1
    assert output[0]["name"] == "Third name"

    keywords = ["yummy"]
    ingredients_to_exclude = ["one"]
    output = search(keywords=keywords, ingredients_to_exclude=ingredients_to_exclude, recipes_file_path=TEST_DB_PATH)

    output = list(output)
    assert len(output) == 1
    assert output[0]["name"] == "Third name"


def test_search_large_data():
    output = search(recipes_file_path=LARGE_DATA_DB_PATH)
    assert next(output)
