#written 11/25/2020
import numpy as np
import sys

#functions expects 3 arguments: 2 samples and 1 flag
#assumes the samples are 1d numpy array
def Function6(x1,x2,flag):
    writtenBy = "Alan Chu"
    #sorts the two sample array
    x1 = np.sort(x1)
    x2 = np.sort(x2)

    Length = len(x1)
    #records the place of counter for each sample array
    i1 = 0
    i2 = 0

    #records the y values to calculate the difference
    y1 = 0
    y2 = 0
    

    increment = 1/Length
    TotalD = 0
    MaxD = 0
    D = 0
    
    #cycles through both cycle from smallest to largest value
    #depending on which sample it is from, it will recalculate the y values and then the difference
    while (i1 != Length or i2 != Length) :
        #index bound control
        if(i1 == Length):
            i2+=1
            y2 += increment
        elif(i2 == Length):
            i1+=1
            y1+=increment
        elif(x1[i1] <= x2[i2]):
            if(i1 < Length):
                i1+=1
                y1 += increment       
        else:
            if(i2 < Length):
                i2+=1
                y2+=increment
        D = abs(y2 - y1)
        TotalD += D
        if(D > MaxD):
            MaxD = D
        print(i1)
        print(i2)
    
    if(flag == 1):
        return MaxD
    if(flag == 2):
        return (TotalD/(2*Length))

    #depending on the flag, it will either display out the the classical or the total ks


