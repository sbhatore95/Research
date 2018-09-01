import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel

import re
import numpy as np
																																																																																	
from pprint import pprint

import spacy

res = []

for i in range(1,76):
	file = open("../word_files/file"+str(i)+".txt", "r")
	arr = file.read().split('\n')
	res.append(arr)

# Create Dictionary
id2word = corpora.Dictionary(res)

# Create Corpus
texts = res

# Term Document Frequency
corpus = [id2word.doc2bow(text) for text in res]

# print(corpus[:1])

lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                           id2word=id2word,
                                           num_topics=20, 
                                           random_state=100,
                                           update_every=1,
                                           chunksize=100,
                                           passes=10,
                                           alpha='auto',
                                           per_word_topics=True)


pprint(lda_model.print_topics())
