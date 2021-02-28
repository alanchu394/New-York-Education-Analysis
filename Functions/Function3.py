#written 10/23/2000


import numpy as np

#assumes 1d numpy array,paramter, and window as inputs respectively for mean and STD
#if the p=3, then it will check if it is a 2d array
def Function3(data,p,n):
    writtenBy = "Alan Chu"
    L = len(data)
    i =0
    j = n
    if data.ndim == 2:
                L = len(data[0])
    answer = list()

    #checks if window size is larger thant the data length
    if n > L:
        return("invalid window size")

    #uses a while loop to iterate each window by incrementing i and j
    #i is the start of the window while j is the end of it
    while j <= L:
        #depending on the parameter(p), the mean std, or correlation will be calculated

        if p == 1:
            #calcuales mean and assigns it to answer array
            answer.append(np.mean(data[i:j]))

        elif p == 2:
            #calculates std and assigns it to answer array
            answer.append(np.std(data[i:j]))

        elif p == 3:
            if data.ndim != 2:
                return("Invalid dimensions of data")
            #calculates the correlation between the windows
            #because the np.corrcoef  returns an array, we only want the element that gives the correlation between the separate vectors
            answer.append(np.corrcoef(data[i:j], rowvar=False) [0][1])

        #increments the windows
        i+=1
        j+=1
    return(answer)

#outputs a 1d array of each windowed mean, std, or correlation
