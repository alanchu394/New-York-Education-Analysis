#written 11/9/2020
import numpy as np


#function expects a 1d numpy array as input
def Function5(data):
    writtenBy = "Alan Chu"

    #records the unique value in the u
    #records the count of each unique value in the c
    u, c = np.unique(data, return_counts=True)
    
    #in a reverse order so that it returns in ascending order
    answer = np.asarray((u[::-1], c[::-1]))
    return answer.T
test = np.array([7,7,7,8,8,8,1,1,1,1,2,2,2,10,10,2,2,3,3,4,4,4,5,6,6])
print(Function5(test))


#Function outputs a 2d array of the unique values and its count
