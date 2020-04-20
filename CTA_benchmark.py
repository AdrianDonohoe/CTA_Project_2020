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

#array_size = [100, 250, 500, 750, 1000, 1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000]
array_size = [100,250,500,750,1000,1250] # for testing

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

# Adapted from https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-10.php
def countingSort(array1):
    m = len(array1) 
    count = [0] * m   # make an array with m elements containing 0             
    
    for a in array1: # itareate over the array to be sorted
    # count occurences of a and increment the count array element for that a
        count[a] += 1             
    i = 0
    for a in range(m):    # iterate over values of the array to be counted        
        for c in range(count[a]):  # fill the array to be counted with count[a] times value a 
            array1[i] = a
            i += 1
    return array1

# Adapted from https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheInsertionSort.html
def insertionSort(alist):
   for index in range(1,len(alist)): # Assume 1st element is sorted, so iterate from 1 to end of array

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue: # This loop will compare  current position against all previous elements and swap them if current position is less than previous element, until postion is 0.
         alist[position]=alist[position-1] # swap with previous element if loop condition met
         position = position-1 # decrement position , so in next loop it will now be compared with previous element

     alist[position]=currentvalue # Second part of the swap (if swapping) or just assigning the same value if not swapping

# Adapted from https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheSelectionSort.html
def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

def main():
    for i in range(0,len(array_size)):
        total_time_bubble = 0
        total_time_merge = 0
        total_time_counting = 0
        total_time_insertion = 0
        total_time_selection = 0
        print("array size: " + str(array_size[i]))
        for j in range(10):
            my_array_bubble = random_array(array_size[i]) 
            my_array_merge = list(my_array_bubble) # Adapted from https://stackoverflow.com/a/2612815
            my_array_counting = list(my_array_bubble)
            my_array_insertion = list(my_array_bubble)
            my_array_selection = list(my_array_bubble)

            # do the Bubble Sort
            print(my_array_bubble)
            start_time_bubble = time.time()
            bubbleSort(my_array_bubble)
            finish_time_bubble = time.time()
            print(my_array_bubble)
            time_elapsed_bubble = finish_time_bubble - start_time_bubble
            print('Run number ' + str(j) + ' ', time_elapsed_bubble)
            total_time_bubble += time_elapsed_bubble

            # do the Merge Sort
            print(my_array_merge)
            start_time_merge = time.time()
            mergeSort(my_array_merge)
            finish_time_merge = time.time()
            print(my_array_merge)
            time_elapsed_merge = finish_time_merge - start_time_merge
            print('Run number ' + str(j) + ' ', time_elapsed_merge)
            total_time_merge += time_elapsed_merge

            # do the Counting Sort
            print(my_array_counting)
            start_time_counting = time.time()
            countingSort(my_array_counting)
            finish_time_counting = time.time()
            print(my_array_counting)
            time_elapsed_counting = finish_time_counting - start_time_counting
            print('Run number ' + str(j) + ' ', time_elapsed_counting)
            total_time_counting += time_elapsed_counting

            # do the Insertion Sort
            print(my_array_insertion)
            start_time_insertion = time.time()
            insertionSort(my_array_insertion)
            finish_time_insertion = time.time()
            print(my_array_insertion)
            time_elapsed_insertion = finish_time_insertion - start_time_insertion
            print('Run number ' + str(j) + ' ', time_elapsed_insertion)
            total_time_insertion += time_elapsed_insertion

            # do the Selection Sort
            print(my_array_selection)
            start_time_selection = time.time()
            selectionSort(my_array_selection)
            finish_time_selection = time.time()
            print(my_array_selection)
            time_elapsed_selection = finish_time_selection - start_time_selection
            print('Run number ' + str(j) + ' ', time_elapsed_selection)
            total_time_selection += time_elapsed_selection


        print('Bubble Sort Total time: ', total_time_bubble)
        print('Merge Sort Total time: ', total_time_merge)
        print('Counting Sort Total time: ', total_time_counting)
        print('Insertion Sort Total time: ', total_time_insertion)
        print('Selection Sort Total time: ', total_time_selection)
    
        times_df.iat[0,i] = round((total_time_bubble/10),3)
        times_df.iat[1,i] = round((total_time_merge/10),3)
        times_df.iat[2,i] = round((total_time_counting/10),3)
        times_df.iat[3,i] = round((total_time_insertion/10),3)
        times_df.iat[4,i] = round((total_time_selection/10),3)

        print('Bubble Sort Avg: ', times_df.iat[0,i])
        print('Merge Sort Avg: ', times_df.iat[1,i])
        print('Counting Sort Avg: ', times_df.iat[2,i])
        print('Insertion Sort Avg: ', times_df.iat[3,i])
        print('Selection Sort Avg: ', times_df.iat[4,i])

    with pd.option_context('display.max_rows', None, 'display.max_columns', None): # Pretty print of Dataframe. Adapted from https://stackoverflow.com/a/30691921
        print(times_df)


if __name__ == "__main__":
    main()

