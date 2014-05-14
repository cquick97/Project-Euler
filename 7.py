'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

import time
start_time = time.time()

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True

number = 2	# 2 is first prime number
flag = 0

while flag <= 10001:
	if isPrime(number):
		flag += 1
		if flag == 10001:
			print(number)
			print("Time elapsed: ", (time.time() - start_time), "seconds")
	number += 1