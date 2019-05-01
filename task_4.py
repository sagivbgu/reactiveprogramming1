import json


def search(file_name, *args):
    keywords, ingredients_to_include, ingredients_to_exclude = _parse_args(args)

    def keywords_filter(recipe):
        def is_keyword_in_field(keyword, field):
            if isinstance(field, (list, dict)) and field:
                return any(is_keyword_in_field(keyword, subfield) for subfield in field)
            return keyword in field

        return all(any(is_keyword_in_field(keyword, recipe[field]) for field in recipe)
                   for keyword in keywords)

    def include_filter(recipe):
        return all(ingredient in recipe["ingredients"] for ingredient in ingredients_to_include)

    def exclude_filter(recipe):
        return not any(ingredient in recipe["ingredients"] for ingredient in ingredients_to_exclude)

    def all_filters(recipe):
        return all(f(recipe) for f in (keywords_filter, include_filter, exclude_filter))

    recipes = _deserialize_recipes_json(file_name)
    return filter(all_filters, recipes)


def statistics(aggregate_function, data, property=None):
    function_data = (recipe[property] if property else recipe for recipe in data)
    return aggregate_function(function_data)


def _parse_args(args):
    def is_include_arg(arg):
        return arg.startswith("+")

    def is_exclude_arg(arg):
        return arg.startswith("-")

    keywords = [arg for arg in args if not is_include_arg(arg) and not is_exclude_arg(arg)]
    ingredients_to_include = [arg[1:] for arg in args if is_include_arg(arg)]
    ingredients_to_exclude = [arg[1:] for arg in args if is_exclude_arg(arg)]

    return keywords, ingredients_to_include, ingredients_to_exclude


def _deserialize_recipes_json(file_path):
    with open(file_path, "r", encoding="utf-8") as recipes_book:
        for line in recipes_book:
            yield json.loads(line)
