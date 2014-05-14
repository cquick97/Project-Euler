'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import time
start_time = time.time()

number = 600851475143
a = 2

while a * a < number:
    while number % a == 0:
        number /= a
    a += 1

print(number)
print("Time elapsed: ", (time.time() - start_time), "seconds")