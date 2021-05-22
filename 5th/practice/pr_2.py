number_lst = [1, 2, 5, 6 , 12, 15]

def square(num):
    return num ** 2

final_result = list(map(square, number_lst))
print(final_result)

