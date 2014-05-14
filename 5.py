'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

import time
start_time = time.time()

a = 20

while a < 250000000:
	if a % 1 == 0 and a % 2 == 0 and a % 3 == 0 \
		and a % 4 == 0 and a % 5 == 0 and a % 6 == 0 \
		and a % 7 == 0 and a % 8 == 0 and a % 9 == 0 \
		and a % 10 == 0 and a % 11 == 0 and a % 12 == 0 \
		and a % 13 == 0 and a % 14 == 0 and a % 15 == 0 \
		and a % 16 == 0 and a % 17 == 0 and a % 18 == 0 \
		and a % 19 == 0 and a % 20 == 0:
		print(a)
		print("Time elapsed: ", (time.time() - start_time), "seconds")
		break
	a += 20 	# Step by 20 because number must be divisable by 20. Greatly reduced time (127 sec > 8 sec)
