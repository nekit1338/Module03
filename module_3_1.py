calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string: str):
    count_calls()
    tuple01 = tuple([len(string), string.upper(), string.lower()])
    return print(tuple01)


def is_contains(string: str, list_to_search: list[str]):
    count_calls()
    string.lower()
    list_to_search = [item.lower() for item in list_to_search]
    return string in list_to_search


string_info("Tokugawa")
string_info("Skirmisher")
result01 = is_contains("bar", ["Baraban", "Bar", "BaMboR"])
result02 = is_contains("Bal", ["BaLaBoL", "Kabala"])
print(result01)
print(result02)
print(calls)
