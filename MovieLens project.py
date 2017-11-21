
import csv
import pandas as pd
import numpy as np
import random
import itertools as it


def boolean_table(df):
	movie = list(sorted(set(df['movieId'].tolist())))
	d = {}
	i = 0
	for x in movie:
    	d[x] = i
    	i+=1
    user_max = len(df['userId'].unique())
    movie_max = len(df['movieId'].unique())
	m = np.zeros(shape = (movie_max, user_max),dtype=np.bool)
	with open('ratings.csv', 'r') as csvfile:
    	reader = csv.reader(csvfile, delimiter = ',')
    	next(reader)
    	for row in reader:
        	if float(row[2]) > 2.5:
            	m[d[int(row[1])], int(row[0]) - 1] = True
    return m

#create a list, with row: user, column: movie liked by user
def user_movie_table(df):
	user_max = len(df['userId'].unique())
	m = []
	for x in range(user_max):
    	a = []
    	m.append(a)
	with open('ratings.csv', 'r') as csvfile:
    	reader = csv.reader(csvfile, delimiter = ',')
    	next(reader)
    	for row in reader:
        	if float(row[2]) > 2.5:
            	m[int(row[0]) - 1].append(int(row[1]))
    return m 

 #calculate similarity in 10000 pairs of users (randomly selected pair) using Jaccard distance formula.
def similarity_user(df,array):
	res = []
	user_max = len(df['userId'].unique())
 	for x in range(10000) :
    	sample = random.sample(range(0, user_max), 2)
    	array1 = array[sample[0]]
    	array2 = array[sample[1]]
    	itersect = len(list(set(array1) & set(array2)))
    	union = len(list(set(array1) | set(array2)))
    	res.append(float(itersect)/union)
    return np.mean(res)

def signature_matrix(inputL,randomNum,prime):
    for i in range(len(inputL)):
        inputL[i] = np.asarray(inputL[i])
    sig_matrix = []
    for user in inputL:
        hash_list = []
        for j in range(randomNum):
            rana = random.randint(1, 8241)
            ranb = random.randint(1, 8241)
            hash_val = np.remainder((rana*user+ranb),prime)
            min_hash = np.amin(hash_val)
            hash_list.append(min_hash)
        sig_matrix.append(hash_list)
    return sig_matrix

def hash_band(r,b,prime,signature_matrix):
    band_matrix = []
    for j in range(b):
        band = sig[(j)*r:(j+1)*r]
    #138449#353#2677
        rana = random.randint(1, prime)
        ranb = random.randint(1, prime)
        hash_val = np.remainder((rana*band+ranb),prime)
        sum_hash = np.sum(hash_val, axis=0)
        band_matrix.append(sum_hash)
    return band_matrix

def bucket(band_matrix):
    dic = {}
    band = band_matrix
    for k in range(len(band)):
        if band[k] not in dic:
            dic[band[k]] = []
        dic[band[k]].append(k)
    return dic

def sim(array1,array2):
    itersect = len(list(set(array1) & set(array2)))
    union = len(list(set(array1) | set(array2)))
    return float(itersect)/union


 def hash_band(r,b,prime,signature_matrix):
    band_matrix = []
    for j in range(b):
        band = sig[(j)*r:(j+1)*r]
    #138449#353#2677
        rana = random.randint(1, prime)
        ranb = random.randint(1, prime)
        hash_val = np.remainder((rana*band+ranb),prime)
        sum_hash = np.sum(hash_val, axis=0)
        band_matrix.append(sum_hash)
    return band_matrix

 def bucket(band_matrix):
    dic = {}
    band = band_matrix
    for k in range(len(band)):
        if band[k] not in dic:
            dic[band[k]] = []
        dic[band[k]].append(k)
    return dic

 def sim(array1,array2):
    itersect = len(list(set(array1) & set(array2)))
    union = len(list(set(array1) | set(array2)))
    return float(itersect)/union

 def similar_user(dic):
 	s = set()
	for k,v in dic.items():
    	if len(v) >= 2:
        	set1 = it.combinations(v,2)
        	for elem in set1:
            	if sim(m[elem[0]], m[elem[1]]) > 0.65:
                	s.add(elem)
    return s

def findNeighbor(elem, dic):
    values = dic.values()
    if elem not in [x for v in values for x in v if type(v)==list]:
        return None
    a = []
    for key,value in dic.items():
        if elem in value:
            a = value
            break
    a.remove(elem)
    res = []
    for i in a:
        similarity = sim(array(elem),array(a[i]))
        res.append(similarity)
    res.sort(reverse=True)
    return res[0]

#-----------------------------main function------------------------------------
if __name__ == '__main__':
    print ('Hello word')
    #read csv file using pandas and get a dataframe csvF
    csvF = pd.read_csv('ratings.csv')
    #create user movie list
    arr = user_movie_table(csvF)
    #calculate similarity
    sim = similarity_user(csvF,arr)

    sig_matrix = signature_matrix(m,1000,8243)
    band_matrix = hash_band(10,100,353,sig)
    dic = bucket(band_matrix[0])
    similar_pair = similar_user(dic)





 






