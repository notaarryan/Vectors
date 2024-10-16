__package__
import matplotlib.pyplot as plt
import numpy as np
import math

class VectorOperations:
    @staticmethod
    def dotProduct(v1,v2) -> float:
        if len(v1.vector) != len(v2.vector):
            raise Exception("Vectors have to be of the same dimensions")
        else:
            return (v1.i*v2.i)+(v1.j*v2.j)+(v1.k*v2.k)
                
    @staticmethod
    def angle(v1,v2):
        if len(v1.vector) != len(v2.vector):
            raise Exception("Vectors have to be of the same dimensions")
        else:
            if VectorOperations.dotProduct(v1,v2) == 0:
                return 90
            elif VectorOperations.dotProduct(v1,v2) == 1:
                return 0
            else:
                dot = VectorOperations.dotProduct(v1,v2)
                mag1,mag2 = v1.mag(),v2.mag()
                return math.degrees(math.acos(dot/(mag1*mag2)))
                
class TwoDVector(VectorOperations):
    try:
        def __init__(self,i=0,j=0):
            self.i = i
            self.j = j
            self.k = 0
            self.vector = [i,j]
            self.xpoint = np.array([0,i])
            self.ypoint = np.array([0,j])
    except TypeError as e:
        print(e)

    def plot(self):
        plt.plot(self.xpoint,self.ypoint)
        plt.show()

    def mag(self):
        return ((self.i**2)+(self.j**2))**0.5
    
class ThreeDVector(TwoDVector):
    
    def __init__(self, i=0, j=0, k=0):
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

    def cross_product(v1, v2):
        if len(v1.vector) != len(v2.vector):
            raise ValueError("Both vectors must have exactly 3 elements.")
        
        cross_prod = [
            v1.vector[1] * v2.vector[2] - v1.vector[2] * v2.vector[1],
            v1.vector[2] * v2.vector[0] - v1.vector[0] * v2.vector[2],
            v1.vector[0] * v2.vector[1] - v1.vector[1] * v2.vector[0]
        ]
    
        return cross_prod 

if __name__ == "__main__":
    pass 