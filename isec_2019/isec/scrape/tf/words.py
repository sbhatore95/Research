# In this file, I take the html files created for the first 100 links and convert them to text
# 24.08.18

from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import codecs
import html2text
res = []
for i in range(1,78):
	with codecs.open("html_files/file" + str(i) + ".html", "r",encoding='utf-8', errors='ignore') as file:
		# file = open("html_files/file" + str(i) + ".html", "r")
		file2 = open("txt_files/file" + str(i) + ".txt", "w")
		r = file.read()
	# example_sent = r

	# stop_words = set(stopwords.words('english'))
	# word_tokens = word_tokenize(example_sent)
	# filtered_sentence = [w for w in word_tokens if not w in stop_words]

	# r = filtered_sentence

	file2.write(html2text.html2text(r))
	file2.close()
	#lis = r.split(' ')
	# counts = Counter(lis)
	# res.append(counts)
# file = open("op", "w")
# for i in res:
# 	file.write(res[i])
# file.close()
