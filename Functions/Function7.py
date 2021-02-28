#written 11/30/2020
import numpy as np

#functions takes in 4 arguments
#1: the prior probability of A
#2: the prior probability of B
#3: the probability of B given A
#4: flag to distuinig simple vs bayes theorem
def Function7(a,b,c,d):
    writtenBy = "Alan Chu"
    if(d == 1):
        #uses simple formula
        return (a*c)/b
    else:
        #uses bayes formula
        x = (c * a) + (b * (1-a))
        answer = (a * c)/x
        return answer
print(Function7(.3,.25,.5,2))


#the functions outputs the posterior probability of A given B
