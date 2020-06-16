#!/usr/bin/python3

import numpy as np
from time import time, sleep
import matplotlib.pyplot as plt

class NeuralNetwork(object):
    def __init__(self, x, y, eta, x_test):
        self.input = x
        self.weights1 = np.random.rand(100, self.input.shape[1])
        self.weights2 = np.random.rand(1, 100)
        self.y = y
        self.output = np.zeros(self.y.shape)
        self.eta = eta
        self.x_test = x_test

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1.T))
        self.output = relu(np.dot(self.layer1, self.weights2.T))

    def feedforward_sin(self):
        self.layer1 = np.tanh(np.dot(self.input, self.weights1.T))
        self.output = np.tanh(np.dot(self.layer1, self.weights2.T))

    def backprop(self):
        delta2 = (self.y - self.output) * relu_derivative(self.output)
        d_weights2 = self.eta * np.dot(delta2.T, self.layer1)
        delta1 = sigmoid_derivative(self.layer1) * np.dot(delta2, self.weights2)
        d_weights1 = self.eta * np.dot(delta1.T, self.input)
        self.weights1 += d_weights1
        self.weights2 += d_weights2

    def backprop_sin(self):
        delta2 = (self.y - self.output) * tanh_derivative(self.output)
        d_weights2 = self.eta * np.dot(delta2.T, self.layer1)
        delta1 = tanh_derivative(self.layer1) * np.dot(delta2, self.weights2)
        d_weights1 = self.eta * np.dot(delta1.T, self.input)
        self.weights1 += d_weights1
        self.weights2 += d_weights2
    
    def train(self):
        plt.ion()
        for i in range(200001):
            self.feedforward()
            self.backprop()
            if i%1000 == 0:
                plt.clf()
                plt.title('Krok {}k'.format(int(i/1000)))
                plt.scatter(self.input[:,0], self.y, s=2)
                plt.scatter(self.x_test[:,0], self.predict(self.x_test), s=2)
                plt.show()
                plt.pause(0.01)

    def train_sin(self):
        plt.ion()
        for i in range(250001):
            self.feedforward_sin()
            self.backprop_sin()
            if i%1000 == 0:
                plt.clf()
                plt.title('Krok {}k'.format(int(i/1000)))
                plt.scatter(self.input, self.y, s=2)
                plt.scatter(self.x_test, self.predict_sin(self.x_test), s=2)
                plt.show()
                plt.pause(0.01)
        print(self.output)

    def predict(self, x):
        pred = sigmoid(np.dot(x, self.weights1.T))
        return relu(np.dot(pred, self.weights2.T)) 

    def predict_sin(self, x):
        pred = np.tanh(np.dot(x, self.weights1.T))
        return np.tanh(np.dot(pred, self.weights2.T)) 

def sigmoid(x):
    return 1.0/(1.0+np.exp(-x))

def sigmoid_derivative(x):
    return x*(1.0-x)    

def relu(x):
    return x * (x > 0)

def relu_derivative(x):
    return 1.0 * (x > 0)

def tanh_derivative(x):
    return 1 - x**2

def teach_parable():
    X = np.linspace(-50, 50, 26)
    x = np.array([[arg, 1.0] for arg in X])
    y = np.array([[arg**2] for arg in X])
    arg = np.linspace(-50,50,101)
    x_test = np.array([[a, 1.0] for a in arg])
    nn = NeuralNetwork(x, y, 0.000001, x_test)
    nn.train()

def teach_sin():
    X = np.linspace(0, 2, 21)
    x = np.array([[arg] for arg in X])
    y = np.array([[np.sin(3*np.pi/2*arg)] for arg in X])
    arg = np.linspace(0,2,161)
    x_test = np.array([[a] for a in arg])
    nn = NeuralNetwork(x, y, 0.005, x_test)
    nn.train_sin()

def main():
    teach_parable()
    teach_sin()

if __name__ == "__main__":
    main()