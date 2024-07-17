def print_params(a=1, b='строка', c=None):
    if c is None:
        c = []
    print(a, b, c)


print_params(1, 2, 3)
print_params(1, 2)
print_params(a=2, c=False)
print_params(b="string", c=2)
print_params()
print_params(b=25)
print_params(c=[4, 5, 6])

values_list = [5, "Abrakadabra", tuple()]
values_dict = {"a": 5, "b": tuple(), "c": frozenset()}
values_list_2 = [20, False]
print_params(*values_list)
print_params(**values_dict)
print_params(42, *values_list_2)
print_params(*values_list_2, 42)
