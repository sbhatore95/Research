# I am trying to get the words that are most prevalent in the discussion of Non performing assets
# lowercase,
# stemming - fish, fishes, fishing into fish
# lemmatisation - gone, going, went into go
import codecs
import re

# To get the numbered strings out of the required ones
def hasNumber(str):
	for i in str:
		if i.isdigit():
			return True
	return False

stopwords = ['are', 'has', 'the', 'after', 'each', "won't", 'an', 'on', "haven't", 'o', 'weren', 'our', "mustn't", "hasn't", 'up', 'needn', 'should', 'shan', 'these', 'with', 'them', 'how', 'during', 'does', 'y', 'ain', 'through', 'any', 'mightn', 'off', 'down', "you'll", 'until', "wouldn't", 'such', 'she', 'ma', 'my', 't', 'being', 'do', "doesn't", 'in', "you'd", 'before', 'if', 'so', 'we', 'they', 'under', "she's", "isn't", "you've", 'won', 'ours', 'out', 'just', "shouldn't", "weren't", 'who', 'a', 'at', 'don', 'didn', "should've", 'again', 'doing', 'own', 'theirs', "it's", 'had', 'mustn', 'for', 'why', "aren't", 'he', "you're", 'wasn', 'd', 'doesn', 'to', 'once', "mightn't", 'which', 'itself', 'haven', "didn't", 'i', 'all', 'into', 'myself', 'while', "hadn't", 'will', 're', 'm', 'over', 'as', 'but', 'its', 've', 'your', 'or', 'is', 'of', 'very', 'what', 'when', 'hadn', 'between', 'ourselves', 'below', 'only', 'hasn', 'wouldn', 'above', 'from', 'most', 'can', 'by', 'were', 'having', 'about', 'been', 'isn', 'than', 'more', 'am', 'himself', 'and', 'hers', 's', 'where', 'now', 'be', 'those', "don't", 'have', 'some', 'me', 'this', 'few', 'against', 'his', "wasn't", "shan't", 'll', "needn't", 'because', 'aren', 'yours', 'nor', 'other', 'no', 'yourselves', 'her', 'not', 'their', 'same', 'themselves', 'whom', "that'll", 'couldn', 'shouldn', 'that', 'you', "couldn't", 'yourself', 'then', 'too', 'further', 'there', 'did', 'him', 'herself', 'it', 'both', 'here', 'was']
res = []
for i in range(1,78):
	with codecs.open("txt_files/file" + str(i) + ".txt", "r",encoding='utf-8', errors='ignore') as file:
		r = file.read()
	wordList = re.sub("[^\w]", " ",  r).split()
	res = res + wordList

file = open("ans.txt", "w")
file2 = open("new.txt", 'w')
for i in res:
	if i.lower() not in stopwords:
		if len(i) > 1 and (not i.isdigit()) and (not hasNumber(i)):
			file.write(i.lower())
			file.write('\n')
			file2.write(i.lower())
			file2.write(' ')

file.close()

file2.close()
