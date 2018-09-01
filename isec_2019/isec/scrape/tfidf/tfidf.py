from sklearn.feature_extraction.text import TfidfVectorizer
corpus = []
for i in range (1, 76):
	file = open("../word_files/file"+str(i)+".txt", "r")
	corpus.append(file.read())
vectorizer = TfidfVectorizer(min_df=1)
X = vectorizer.fit_transform(corpus)
idf = vectorizer.idf_
dic = dict(zip(vectorizer.get_feature_names(), idf))
s = [(k, dic[k]) for k in sorted(dic, key=dic.get)]
file = open("ans.txt", "w")
file2 = open("ans2.txt", "w")
for key, value in s:
	file.write(str(value)+'\n')
	file2.write(key+'\n')
# print(s)