#written 12/17/2020
import numpy as np

#takes in 1 arugument of an 1d numpy array

def FunctionXC(data):   
    writtenBy = "Alan Chu"
    for i in range(len(data)):
        
        if(np.isnan(data[i])):

            #checks if next value is also null
            if(np.isnan(data[i+1])):
                #records consecutive Nan values
                counter = 0
                while(True):
                    if(np.isnan(data[i+counter])==False):
                        break
                    counter += 1
                #uses np.linspace to interpolate
                y = np.linspace(data[i-1], data[i+counter], num=counter+2)
                data[i-1:i+counter+1] = y

            else:
                #averages 
                data[i] = (data[i-1]+data[i+1])/2

    return data

#returns interpolated 1d numpy array