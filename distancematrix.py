import numpy as np
import math
def create_distance_matrix(cities):
    n = len(cities)
    matrix= np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist=math.sqrt((cities[i][0]-cities[j][0])**2 + (cities[i][1]-cities[j][1])**2)
            matrix[i][j]=matrix[j][i]=dist
    return matrix
   