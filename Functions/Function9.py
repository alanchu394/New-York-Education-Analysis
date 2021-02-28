#written 12/17/2020

import numpy as np
import pandas as pd



df = pd.read_csv("sampleConfusion1.csv")  
#written 12/17/2020
#takes in 4 arguments: xbase, null distribution, signal distribution, threshhold value x
def Function9(xBase, nullDis, sigDis, threshhold):
    writtenBy = "Alan Chu"
    #find the index of the threshhold in xBase
    index = np.where(xBase == threshhold)[0][0]

    #Calculate the true positives as the sum of all values in the signal distribution 
    truePos = 0;
    for i in range(index+1,len(sigDis)):
        truePos += sigDis[i]

    #Calculate the false positives as the sum of all values in the null distribution 
    falsePos = 0;
    for i in range(index+1,len(nullDis)):
        falsePos += nullDis[i]
    
    #Calculate the false negatives as the sum of all values in the signal distribution
    falseNeg = 0
    for i in range(0,index+1):
        falseNeg += sigDis[i]

    #Calculate the true negatives as the sum of all values in the null distribution
    trueNeg = 0;
    for i in range(0,index+1):
        trueNeg += nullDis[i]
    answer = ([truePos,falsePos],[falseNeg,trueNeg])
    return answer


#computes the full 2x2 confusion matrix: True positives, false positives, false negatives and true negatives 

a= df["A"]
b= df["B"]
c= df["C"]

print(Function9(a,b,c,2))
    









