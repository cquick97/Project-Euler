'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''
import time
start_time = time.time()

max_len = 0
a = 1000000	

while a > 1:
	n = [a]

	while n[len(n)-1] > 1:
		if n[len(n)-1] % 2 == 0:
			n.append(n[len(n)-1] / 2)
		elif n[len(n)-1] % 2 != 0:
			n.append(3 * n[len(n)-1] + 1)
	print(n[0], max_len)
	if len(n) > max_len:
		max_len = len(n)
		number = n[0]
	a = a - 1
print("max_len = ", max_len, "Number = ", number)	
print("Time elapsed: ", time.time()	- start_time