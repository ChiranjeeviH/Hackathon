
# coding: utf-8

# In[4]:


import pandas as pd
import argparse
from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import operator



ap = argparse.ArgumentParser()
ap.add_argument("-d", "--test_data", required=True,
   help="provide test data")

args = vars(ap.parse_args())
print('input provided-- ', args['test_data'])

train=pd.read_csv('train_news.csv', encoding='utf-8')

google_model=KeyedVectors.load_word2vec_format('/home/merit/Dhirendra/BIP/model/GoogleNews-vectors-negative300.bin',binary=True)

def sent_to_vec(sent, google_model, dim=300):
    vect = np.zeros(300)
    count = 0
    if sent is not '':
        for word in sent.split():
            if word in google_model:
                vect = vect + google_model[word]
            else:
                count = count + 1
                if (count == len(sent.split())):
                    return np.zeros(300)

    return vect / ((len(sent.split()) - count))

train_vector=[]
for news in train.news_title:
	train_vector.append(sent_to_vec(news, google_model))


test_vector=sent_to_vec(args['test_data'], google_model)

sim_list=cosine_similarity(train_vector,test_vector.reshape(1,-1))
score_list= sorted(enumerate(sim_list), key=operator.itemgetter(1),reverse=True)[:1]
#print(score_list)
#print(score_list[0])
#print(score_list[0][1])
if score_list[0][1] > 0.8:
    print("alert--this is a dublicate news")
    print("matched with training records having index= ",score_list[0][0])
