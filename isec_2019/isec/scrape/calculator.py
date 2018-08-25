# let's calculate frequencies of the words in lemma.txt

file = open("lemma.txt", 'r')
res = file.read().split('\n')

file = open("frequencies.txt", 'w')
over = []
dic = {}

for i in res:
	if i in over:
		dic[i] = dic[i] + 1
	else:
		dic[i] = 1
		over.append(i)
s = [(k, dic[k]) for k in sorted(dic, key=dic.get, reverse=True)]
for key, value in s:
	file.write(str(value) + " " + key + '\n')