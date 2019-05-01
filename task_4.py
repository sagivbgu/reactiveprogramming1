import json


def search(file_name, keywords=(), ingredients_to_include=(), ingredients_to_exclude=()):
    def keywords_filter(recipe):
        return all(any(keyword in recipe[field] for field in recipe)
                   for keyword in keywords)

    def include_filter(recipe):
        return all(ingredient in recipe["ingredients"] for ingredient in ingredients_to_include)

    def exclude_filter(recipe):
        return not any(ingredient in recipe["ingredients"] for ingredient in ingredients_to_exclude)

    def all_filters(recipe):
        return all(f(recipe) for f in (keywords_filter, include_filter, exclude_filter))

    recipes = _deserialize_recipes_json(file_name)
    return filter(all_filters, recipes)


def statistics(function, properties, data):
    properties_values = (int(recipe[properties]) for recipe in data if properties in recipe)
    return function(properties_values)


def _deserialize_recipes_json(file_path):
    with open(file_path, "r", encoding="utf-8") as recipes_book:
        for line in recipes_book:
            yield json.loads(line)
