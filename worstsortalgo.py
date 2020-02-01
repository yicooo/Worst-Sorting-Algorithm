from random import randrange
import timeit

start = timeit.default_timer()

def swap1(arr,x,y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp

arr = [1,2,3,7,4,9,1,4,15,61,1,23,41,4,1,2,3,5,7,7,1,8,9,6,4,3,34,2,2,5,1,1233,41,31,51,654,745,73,45,2,34,124,12,41,2,121]
iterationCount = 0

while True:
    iterationCount = iterationCount+1
    flag = 0
    randIndex = randrange(len(arr))
    element = arr[randIndex]
    randIndex2 = randrange(len(arr))
    element2 = arr[randIndex2]
    if randIndex2 > randIndex:
        if element2 < element:
            swap1(arr,randIndex,randIndex2)
    
    elif randIndex2 < randIndex:
        if element2 > element:
            swap1(arr,randIndex,randIndex2)


    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            flag = 1

    if flag == 0:
        print(arr)
        print("arr is sorted")
        print("iteration count:", end='')
        print(iterationCount)
        break

stop = timeit.default_timer()

print('Time: ', stop - start)  
