'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

import time
start_time = time.time()

a = 100
b = 100
max_palin = 0

while a < 1000:
	b = 100
	while b < 1000:
		c = a * b
		c = str(c)
		if c == c[::-1]:
			if int(c) > int(max_palin):
				max_palin = c
		b += 1
	a += 1

print(max_palin)
print("Time elapsed: ", (time.time() - start_time), "seconds")