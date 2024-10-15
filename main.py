import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

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
    
class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
        self.vector = [i,j,k]
        self.xpoint = np.array([0,i])
        self.ypoint = np.array([0,j])
        self.zpoint = np.array([0,k])
    
    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111,projection="3d")
        ax.plot(self.xpoint,self.ypoint,self.zpoint,label = "3D Line")
        ax.legend()
        ax.set_xlabel('X Axis')
        ax.set_ylabel('Y Axis')
        ax.set_zlabel('Z Axis')
        plt.show()

v = ThreeDVector(1,2,3)
v.plot()