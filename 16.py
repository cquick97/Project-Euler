'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

import math
import time
start_time = time.time()

number = str(pow(2, 1000))
lst = []
for i in number:
	lst.append(int(i))
print(sum(lst))
print("Time elapsed: ", time.time() - start_time, "seconds")
