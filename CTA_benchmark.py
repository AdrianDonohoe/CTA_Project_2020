# Created by Adrian Donohoe 17/04/2020 following testing on jupyter notebook
# https://github.com/AdrianDonohoe/CTA_Project_2020/blob/master/CTA%20Project%202020.ipynb


import time
import numpy as np
import pandas as pd

def random_array(n):
    array = []
    for i in range(0,n,1):
        array.append(np.random.randint(0,100))
    return array

# Make a dataframe for outputting
cols = ['n=100','n=250','n=500','n=750','n=1000','n=1250','n=2500','n=3750','n=5000','n=6250','n=7500','n=8750','n=10000']
indexes = ['bubble', 'merge', 'counting', 'insertion','selection']
times_df =  pd.DataFrame(index=indexes,columns=cols)
times_df

array_size = [100, 250, 500, 750, 1000, 1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000]

##################   BubbleSort##################
# adapted from https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheBubbleSort.html
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):   # loop over array from last to first. After the first pass the largest number will be in the last position. Each successive loop will be shorter as the largest number will be at the end and the loop decrements.
        for i in range(passnum): # loop from first to last swapping number with the one after it if first number is greater.
            if alist[i]>alist[i+1]: # Compare item at postion i with item at position i+1
                alist[i], alist[i+1] = alist[i+1], alist[i] # Swap the two items if above condtion is matched


# Adapted from https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheMergeSort.html
def mergeSort(alist):
    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Merging ",alist)



def main():
    ### Call BubbleSort
    for i in range(0,len(array_size)):
        total_time = 0
        print("array size: " + str(array_size[i]))
        for j in range(10):
            my_array = random_array(array_size[i])
            start_time = time.time()
            bubbleSort(my_array)
            finish_time = time.time()
            time_elapsed = finish_time - start_time
            print('Run number ' + str(j) + ' ', time_elapsed)
            total_time += time_elapsed
        print('Total time: ', total_time)
    
        times_df.iat[0,i] = round((total_time/10),3)
        print('Avg: ', times_df.iat[0,i])
    with pd.option_context('display.max_rows', None, 'display.max_columns', None): # Pretty print of Dataframe. Adapted from https://stackoverflow.com/a/30691921
        print(times_df)

    ############ Call MergeSort
    for i in range(0,len(array_size)):
        total_time = 0
        print("array size: " + str(array_size[i]))
        for j in range(10):
            my_array = random_array(array_size[i])
            start_time = time.time()
            mergeSort(my_array)
            finish_time = time.time()
            time_elapsed = finish_time - start_time
            print('Run number ' + str(j) + ' ', time_elapsed)
            total_time += time_elapsed
        #print(my_array)
        print('Total time: ', total_time)
    
        times_df.iat[1,i] = round((total_time/10),3)
        print('Avg: ', times_df.iat[1,i])

    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(times_df)
    


if __name__ == "__main__":
    main()

