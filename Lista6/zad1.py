#!/usr/bin/python3

import numpy as np
from time import time

class NeuralNetwork(object):
    def __init__(self, x, y, fn, fn_der, eta, seed):
        np.random.seed(seed)
        self.fn = fn
        self.fn_der = fn_der
        self.input = x
        self.weights1 = np.random.rand(4, self.input.shape[1])
        self.weights2 = np.random.rand(1, 4)
        self.y = y
        self.output = np.zeros(self.y.shape)
        self.eta = eta
        self.layer1 = self.fn(np.dot(self.input, self.weights1.T))
        self.output = self.fn(np.dot(self.layer1, self.weights2.T))

    def feedforward(self):
        self.layer1 = self.fn(np.dot(self.input, self.weights1.T))
        self.output = self.fn(np.dot(self.layer1, self.weights2.T))

    def backprop(self):
        delta2 = (self.y - self.output) * self.fn_der(self.output)
        d_weights2 = self.eta * np.dot(delta2.T, self.layer1)
        delta1 = self.fn_der(self.layer1) * np.dot(delta2, self.weights2)
        d_weights1 = self.eta * np.dot(delta1.T, self.input)
        self.weights1 += d_weights1
        self.weights2 += d_weights2
    
    def train(self):
        for _ in range(5000):
            self.feedforward()
            self.backprop()
        for el in self.output:
            print('{0:.8f}'.format(el[0]), end=' ')
        print()

def sigmoid(x):
    return 1.0/(1+np.exp(-x))

def sigmoid_derivative(x):
    return x*(1.0-x)    

def relu(x):
    return x * (x > 0)

def relu_derivative(x):
    return 1.0 * (x > 0)

def combine(x):
    return relu(sigmoid(x))

def combine_derivative(x):
    return relu_derivative(sigmoid(x))*sigmoid_derivative(x)

def teach():
    op = ['Teaching XOR:', 'Teaching OR:', 'Teaching AND:']
    X = np.array([[0,0,1], [0,1,1], [1,0,1], [1,1,1]])
    Y = [np.array([[0],[1],[1],[0]]), np.array([[0],[1],[1],[1]]), np.array([[0],[0],[0],[1]])]
    for i in range(3):
        print(op[i])
        print('\ty:', end=' ')
        for el in Y[i]:
            print(el[0], end=' ')
        print()
        nn_si = NeuralNetwork(X, Y[i], sigmoid, sigmoid_derivative, 0.5, int(time()))
        nn_re = NeuralNetwork(X, Y[i], relu, relu_derivative, 0.01, 17)
        nn_co = NeuralNetwork(X, Y[i], combine, combine_derivative, 0.8, 40)
        print('\ttraining using sigmoid:', end=' ')
        nn_si.train()
        print('\ttraining using ReLU:', end=' ')
        nn_re.train()
        print('\ttraining using combination:', end=' ')
        nn_co.train()

def main():
    #w przykładzie jest kolumna z samymi jedynkami, bo pełni ona rolę biasu
    teach()

if __name__ == '__main__':
    main()