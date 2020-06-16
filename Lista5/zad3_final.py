#!/usr/bin/env python3

import numpy as np
import pandas as pd
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import norm

def read_data():
    content = pd.read_csv('ratings.csv', usecols=['userId', 'movieId', 'rating'])
    data = lil_matrix(content)
    sizes = pd.DataFrame.max(content, axis=0)
    prepared = lil_matrix((int(sizes['userId']), int(sizes['movieId'])))

    current_id = 0
    i = 0
    while i < data.shape[0]:
        current_id = int(data[i,0])-1
        while i < data.shape[0] and current_id == int(data[i,0])-1 :
            prepared[current_id, (int(data[i, 1])-1)] = float(data[i, 2])
            i += 1
    return prepared

def get_movies():
    return pd.read_csv('movies.csv', usecols=['movieId', 'title'])

def recommend(x, y):
    np.seterr(all='ignore')
    x = lil_matrix(np.nan_to_num(x/norm(x, axis=0)))
    y = np.nan_to_num(y/norm(y))
    cos_prob = x.dot(y)
    cos_prob = np.nan_to_num(cos_prob/norm(cos_prob))
    rec = np.nan_to_num((x.transpose()).dot(cos_prob))
    prep = [(rec[i, 0], i+1) for i in range(rec.shape[0])]
    prep = sorted(prep, key=lambda t: t[0], reverse=True)
    movies = get_movies()
    print("Tytul, podobienstwo:")
    for i in range(10):
        title = movies[movies['movieId'] == prep[i][1]].to_numpy()
        print('{}, {}'.format(title[0][1], prep[i][0]))

def main():
    x = read_data()
    my_ratings = lil_matrix((x.shape[1],1))
    my_ratings[2570] = 5
    my_ratings[31] = 4
    my_ratings[259] = 5
    my_ratings[1096] = 4
    recommend(x, my_ratings)

if __name__ == "__main__":
    main()
