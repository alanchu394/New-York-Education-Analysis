#written 12/8/2020
import numpy as np


#function expects 2  inputs: a 1d numpy array and a bound
def Function8(data, x):
    writtenBy = "Alan Chu"
    
    #sort the 1d numpy array
    data = np.sort(data)
    length = len(data)

    #calculate lower and upper mass
    lowerM = (100 - x)/2
    upperM = (100- lowerM)

    #find the index 
    lowerI = int(round(lowerM / 100 * length - 1, 0))
    upperI = int(round(upperM / 100 * length - 1, 0))

    #find the index within the data
    a = data[lowerI]
    b = data[upperI]

    return a,b
#function returns the lower and upper bound of the data 