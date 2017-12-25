#A palindromic number reads the same both ways. The largest palindrome made
#from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

#operator: https://docs.python.org/3/library/operator.html
#numpy: https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.transpose.html

#The original problem only requires the palindrome, but I figure it's more meaningful to return the two 3-digit numbers that of which the palindrome is product.

import numpy as np
import operator
result = np.transpose(np.array([[i*j, i, j] for i in range(100, 1000) for j in range(100, 1000) if str(i*j)[::-1] == str(i*j)]))

index, value = max(enumerate(result[0]), key=operator.itemgetter(1))
print(value, result[1][index], result[2][index])
