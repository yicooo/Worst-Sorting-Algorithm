from random import randrange    #To generate random integers within a given range
import timeit                   #To calculate run-time

"""
start variable indicates the starting time of this algorithm.
Later, this variable will be used to calculate run-time
"""
start = timeit.default_timer()

"""
function  swap;
arguments arr , x , y
arr : This is the list which this operation will be held on
x   : Index of one of the items which will be swapped
x   : Index of the other one of the items which will be swapped
No return
"""
def swap1(arr,x,y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp

"""
arr is the input list
arr will be sorted
"""
arr = [1,2,3,7,4,9,1,4,15,61,1,23,41,4,1,2,3,5,7,7,1,8,9,6,4,3,34,2,2,5,1,1233,41,31,51,654,745,73,45,2,34,124,12,41,2,121]

"""
iterationCount variable holds the interation count to be
printed later on
"""
iterationCount = 0

#Main Loop
while True:

    iterationCount = iterationCount+1           #iteration count is incremented
    flag = 0                                    #flag is to determine wheter array is sorted or not
    
    randIndex = randrange(len(arr))             
    element = arr[randIndex]
    #First element is selected randomly
    
    randIndex2 = randrange(len(arr))
    element2 = arr[randIndex2]
    #Second element is selected randomly
    
    if randIndex2 > randIndex:                  #If second item is at the rightside of first item

        if element2 < element:                  #If right-one is smaller

            swap1(arr,randIndex,randIndex2)     #Swap elements

    
    elif randIndex2 < randIndex:                #If second item is at the leftside of first item

        if element2 > element:                  #If right-one is smaller

            swap1(arr,randIndex,randIndex2)     #Swap elements


    for i in range(len(arr)-1):                 #This for loop checks if arr is sorted or not

        if arr[i] > arr[i+1]:
            flag = 1                            #Flag is set to 1 if arr is NOT sorted


    if flag == 0:                               #If arr is sorted
        
        print(arr)
        print("arr is sorted")
        print("iteration count:", end='')
        print(iterationCount)
        break                                   #Get out of the loop it is done!


"""
stop variable indicates the ending time of this algorithm.
Later, this variable will be used to calculate run-time
"""
stop = timeit.default_timer()

print('Time: ', stop - start)  
