import random 
import numpy 

# function for the reservoir

def reservoir_sample(stream, k): # takes two arguments 
    reservoir = [] #intializes an empty list to store our items
    
    for i, item in enumerate(stream): # creates a pair of  i (index) & the item from stream
        if i<k: # checks if i is less than k (our sample size)
            reservoir.append(item) # if so appends the reservoir
        else: # if not 
            j = random.randint(0, i) # creates a random interger btwn 0 and our sample size which is equal to i
            if j<k: # checks if j(index) is in the bounds of the sample size  
                reservoir[j] = item # replaces the new item in thst index
                
    return reservoir # returns the reservoir


# create a stream with our constraints
# generating a data with normal distribution with a mean of 50 and and a std of 10 to simulate a STREAM
stream  = numpy.random.normal(loc=50, scale=10, size=100000)
# print(stream)
# applying our function 
sample = reservoir_sample(stream, 100)


# 