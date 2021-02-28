import numpy as np


#from function 1 assignment, it calculates the Mean Absolute Deviation
def MeanAbsoluteDeviation(data):
    writteBy = "Alan Chu"
    answer = np.mean(np.absolute(data - np.mean(data))) 
    return(answer)
#Input assumes a 1d numpy array
#function calculates Mean, Median, Standard Deviation, MAD, n and SEM
#mean uses np.mean to calculate
#Median uses np.median to calculate
#STD uses np.std to calculate
#MAD uses the function from asssignment 1 to calculate
#n uses len() functiont to calculate
#SEM takes the answer from STD and divides it by the square root of the length
def Function2(data):
    writtenBy = "Alan Chu"
    mean = np.mean(data)
    median = np.median(data)
    STD = np.std(data)
    MAD = MeanAbsoluteDeviation(data)
    n = len(data)
    SEM = STD/(n**.5)

    answer = np.array([mean,median,STD,MAD,n,SEM])
    return(answer)
#Outputs a 1d numpy array with the 6 variables
#written on 10/19/20