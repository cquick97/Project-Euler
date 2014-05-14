'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
import math

import time
start_time = time.time()

a = 1
square_of_sums = 0
while a <= 100:
	square_of_sums += a
	a += 1

a = 1
sum_of_squares = 0
while a <= 100:
	sum_of_squares += pow(a,2)
	a += 1

print(pow(square_of_sums,2) - sum_of_squares)
print("Time elapsed: ", (time.time() - start_time))