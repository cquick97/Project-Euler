'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into 
alphabetical order. Then working out the alphabetical value for each name, 
multiply thisvalue by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN, which
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

import csv
import sys
import time

start_time = time.time()

f = open(sys.argv[1], 'rt')
names_list = list()

try:
    reader = csv.reader(f)
    reader_list = list(reader)
finally:
    f.close()

for n in range(0,5163):
	names_list.append(reader_list[0][n])

names_list.sort()

total = 0

for n in range(0,5163):
	current_name = names_list[n]
	current_name_list = list(current_name)


	for i in range(len(current_name_list)):
		current_name_list[i] = current_name_list[i].lower()
		total += (int(ord(current_name_list[i]) - 96) * (n+1))

print(total)
print("Time elapsed: ", (time.time() - start_time))