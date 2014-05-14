'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

import time
start_time = time.time()

n = 1
total = 0

while n < 1000:
	if n % 3 == 0:
		total += n
	elif n % 5 == 0:
		total += n
	n += 1
print(total)
print("Time elapsed: ", (time.time()-start_time), "seconds")
