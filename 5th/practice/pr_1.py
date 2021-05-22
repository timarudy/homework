def lower(string_low):
    new_string_1 = string_low.lower()
    return new_string_1

def upper(string_up):
    new_string_2 = string_up.upper()
    return new_string_2

lst_1 = ["Tedd went to the yard.", "Less go! Dababy!"]
lst_2 = ["Nice value!", "Whats up ma man?"]

final_func_1 = list(map(lower, lst_1))
final_func_2 = list(map(upper, lst_2))
print(final_func_1)
print(final_func_2)

