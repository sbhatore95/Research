# Code to eliminate all the words not in english dictionary
# 25.08.18

file = open("new.txt", 'r')
res = file.read().split(' ')
import enchant
d = enchant.Dict("en_US")
file = open("new1.txt", 'w')
for i in res:
	if i is not '':
		if d.check(i):
			file.write(i)
			file.write('\n')
file.close()