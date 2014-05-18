'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
'''

import time
from num2words import num2words

start_time = time.time()

sum_of_letters = 0
n = 1

while n <= 1000:
	words = num2words(n)
	words = words.replace(' ', '')
	words = words.replace('-', '')
	sum_of_letters += len(words)
	n += 1

print(sum_of_letters)
print("Time elapsed: ", (time.time() - start_time), "seconds")