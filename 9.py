'''
Project Euler Problem 9
Language: Python 3.4

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import time
import math

start_time = time.time()

for a in range(1,500):
	for b in range(a,500):
		for c in range(b,500):
			if math.pow(a,2) + math.pow(b,2) == math.pow(c,2) and a + b + c == 1000:
				print(a*b*c)

print("Time elapsed: ", (time.time() - start_time), "seconds")
