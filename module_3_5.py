def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result = get_multiplied_digits(10203)  # -> 6
result01 = get_multiplied_digits(40506)  # -> 120
result02 = get_multiplied_digits(70809)  # -> 504
result03 = get_multiplied_digits(405060)  # -> 0
print(result)
print(result01)
print(result02)
print(result03)