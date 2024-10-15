import matplotlib.pyplot as plt
import numpy as np

class VectorOperations:
    pass

class TwoDVector(VectorOperations):
    def __init__(self,i,j):
        self.i = i
        self.j = j
        self.vector = [i,j]
        self.xpoint = np.array([0,i])
        self.ypoint = np.array([0,j])

    def plot(self):
        plt.plot(self.xpoint,self.ypoint)
        plt.show()

    def mag(self):
        return ((self.i**2)+(self.j**2))**0.5