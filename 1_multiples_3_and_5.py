"""

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

TASK: Find the sum of all the multiples of 3 or 5 below 1000.

"""

import numpy as np


def sum_multiples_of(up_to_value, x, y):


    arg_product = x*y

    arg_poduct_sum = sum(list(range(1, (up_to_value - 1) // arg_product + 1)))*arg_product


    def arg_multiples(x1, limit):
        rep = (limit-1)//x1
        return x1*rep*(rep+1)/2

    return arg_multiples(x, up_to_value) + arg_multiples(y, up_to_value) - arg_poduct_sum

print(sum_multiples_of(1000, 3, 5))