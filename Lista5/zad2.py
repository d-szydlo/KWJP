#!/usr/bin/bash

import numpy as np
import csv

def get_data():
    data = []
    with open('ratings.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    data = data[1:]
    i = 0
    filtered = []
    while i < len(data):
        num = data[i][0]
        row = [0 for _ in range(10000)]
        while i < len(data) and data[i][0] == num:
            if int(data[i][1]) < 10001:
                row[int(data[i][1])-1] = float(data[i][2])
            i += 1
        filtered.append(row)
    return np.array(filtered)
    
def get_movies():
    data = []
    with open('movies.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                if int(row[0]) < 10001:
                    data.append(row[1])
            except:
                pass
    return data

def recommend(x, y):
    x = np.nan_to_num(x/np.linalg.norm(x, axis=0))
    y = np.nan_to_num(y/np.linalg.norm(y))
    cos_prob = np.dot(x, y)
    cos_prob = np.nan_to_num(cos_prob/np.linalg.norm(cos_prob))
    rec = np.dot(x.T, cos_prob)
    prep = [(rec[i][0], i+1) for i in range(len(rec))]
    prep = sorted(prep, key=lambda t: t[0], reverse=True)
    movies = get_movies()
    print("Tytul, podobienstwo:")
    for i in range(10):
        print('{}, {}'.format(movies[prep[i][1]], prep[i][0]))
    
def main():
    my_ratings = np.zeros((10000, 1))
    my_ratings[2570] = 5
    my_ratings[31] = 4
    my_ratings[259] = 5
    my_ratings[1096] = 4
    x = get_data()
    recommend(x, my_ratings)

if __name__ == "__main__":
    main()