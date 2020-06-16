#!/usr/bin/python

import numpy as np
import csv
import matplotlib.pyplot as plt

def get_data(m):
    data = []
    with open('ratings.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    data = data[1:]
    i = 0
    filtered = []
    toy_story = []
    while i < len(data):
        if data[i][1] == '1':
            num = data[i][0]
            row = [0 for _ in range(m)]
            toy_story.append([float(data[i][2])])
            i += 1
            while i < len(data) and data[i][0] == num:
                if int(data[i][1]) < m+2:
                    row[int(data[i][1])-2] = float(data[i][2])
                i += 1
            filtered.append(row)
        else:
            num = data[i][0]
            while i < len(data) and data[i][0] == num:
                i += 1
    return np.array(filtered), np.array(toy_story)

def lin_reg(x, y):
    col = np.array([np.ones(len(x))]).T
    A = np.hstack((x, col))
    m = np.linalg.lstsq(A, y, rcond=None)[0]
    computed = []
    for row in A:
        val = 0
        for i in range(len(row)):
            val += row[i]*m[i][0]
        computed.append(val)
    mis = []
    for i in range(215):
        mis.append(abs(computed[i]-y[i][0]))
    return mis

def lin_reg_train(x, y):
    toy = np.array([y[i] for i in range(200, 215)])
    usr = np.array([x[i] for i in range(200, 215)])
    for _ in range(15):
        x = np.delete(x, 200, 0)
        y = np.delete(y, 200, 0)
    col = np.array([np.ones(len(x))]).T
    A = np.hstack((x, col))
    m = np.linalg.lstsq(A, y, rcond=None)[0]
    col = np.array([np.ones(len(usr))]).T
    usr = np.hstack((usr, col))
    computed = []
    for row in usr:
        val = 0
        for i in range(len(row)):
            val += row[i]*m[i][0]
        computed.append(val)
    plot_val(toy, computed, len(x[0]))
    
def plot_val(original, predicted, m):
    user = np.arange(1, 16)
    _ = plt.plot(user, original, 'o', label='ocena uzytkownika', markersize=2)
    _ = plt.plot(user, predicted, 'o',label='predykcja', markersize=1)
    _ = plt.legend()
    _ = plt.title('m = {}'.format(m))
    plt.show()
    plt.close()

def plot_dif(dif, lab):
    user = np.arange(1, 216)
    plt.bar(user, dif, label=lab)
    plt.legend()
    plt.title('Bledy dopasowania')
    plt.xlabel('Uzytkownik')
    plt.ylabel('Blad')
    plt.show()
    plt.close()

def part_1():
    val = [10, 1000, 10000]
    for m in val:
        x, y = get_data(m)
        m = lin_reg(x, y)
        plot_dif(m, 'm = {}'.format(m))

def part_2():
    val = [10, 100, 200, 500, 1000, 10000]
    for m in val:
        x, y = get_data(m)
        lin_reg_train(x, y)

def main():
    part_1()
    part_2()

if __name__ == "__main__":
    main()