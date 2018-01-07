

#!/bin/python

from random import randint


sum = 0
cnt = 0
for var in range(1,10000):
	l = randint(0,6)
	m = randint(0,6) 
	if l == m & l == 6 & m == 6:
		print   'Birinci zar :', l , '  Ikinci zar:' , m
		cnt += 1
print cnt

