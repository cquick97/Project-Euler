'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Warning: This solution is not very efficient, and took 30 seconds on my i7 laptop.
'''

import time
start_time = time.time()

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True

n = 2	# 2 is fist prime number, not 1
list_of_primes = []

while n < 2000000:
	if n == 2:
		n += 1
	elif n % 2 == 0:
		n += 1
	else:
		if isPrime(n):
			list_of_primes.append(n)
		n += 1

print(sum(list_of_primes))
print("Time elapsed: ", (time.time() - start_time), "seconds")