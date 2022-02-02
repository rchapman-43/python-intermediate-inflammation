from cgi import test
from functools import reduce

#sequence = [1, 2, 3]

# def product(a,b):
#     return a * b

# print(reduce(product, sequence))
# print(reduce((lambda a, b: a * b), sequence))


def sum_of_squares(sequence):
    integers = [int(x) for x in sequence if x[0] != '#']
    squares = [x * x for x in integers]
    return reduce(lambda a, b: a + b, squares)

# print(sum_of_squares([0]))
# print(sum_of_squares([1]))
# print(sum_of_squares([1, 2, 3]))
# print(sum_of_squares([-1]))
# print(sum_of_squares([-1, -2, -3]))

print(sum_of_squares(['1', '2', '3']))
print(sum_of_squares(['-1', '-2', '-3']))
print(sum_of_squares(['1', '2', '#100', '3']))