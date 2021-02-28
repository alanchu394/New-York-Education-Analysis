#written 11/1/2020

import numpy as np
#Funciton assumes an input of a 2d numpy array and a flag
def Function4(data, flag):
    writtenBy = "Alan Chu"

    #Calculates how many rows
    Length = len(data)
    a = 0
    #Calculates the summation within the function
    for i in range(Length):
        #calculates the absolute value within the summation
        #then put its to the power of the flag
        a += (abs(data[i][0] - data[i][1]))**flag

    #divides the summation total by n
    b = a/ Length

    #takes b and puts it to the power of (1/flag)
    answer = b ** (1/flag)
    return answer
x = np.array([[0,50],[10,5],[5,10]])
print(Function4(x ,3))
#Function outputs a single number
