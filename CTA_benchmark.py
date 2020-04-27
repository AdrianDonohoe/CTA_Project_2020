# Created by Adrian Donohoe 17/04/2020 following testing on jupyter notebook
# https://github.com/AdrianDonohoe/CTA_Project_2020/blob/master/CTA%20Project%202020.ipynb


import time
import numpy as np
import pandas as pd
from tabulate import tabulate # Will use this to prettify the output


# A function to generate random numbers
def random_array(n):
    array = []  # Create an empty list
    for i in range(0,n,1): # Loop over 0 to n i.e. creating n elements in the array
        array.append(np.random.randint(0,100)) # and append a random number between 0 and 99
    return array # return the new array of n elements



##################   BubbleSort##################
# adapted from https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheBubbleSort.html
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):   # loop over array from last to first. After the first pass the largest number will be in the last position. Each successive loop will be shorter as the largest number will be at the end and the loop decrements.
        for i in range(passnum): # loop from first to last swapping number with the one after it if first number is greater.
            if alist[i]>alist[i+1]: # Compare item at postion i with item at position i+1
                alist[i], alist[i+1] = alist[i+1], alist[i] # Swap the two items if above condtion is matched


# Adapted from https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheMergeSort.html
def mergeSort(alist):
    if len(alist)>1: # Check if list can be split
        mid = len(alist)//2  # Floor divide to find roughly middle
        lefthalf = alist[:mid] # Splice from start to mid to make left half
        righthalf = alist[mid:] # Splice from mid to end to make right half

        mergeSort(lefthalf) # Recursive call of mergeSort on lefthalf
        mergeSort(righthalf) # Recursive call of mergeSort on righthalf

        # Variables for positions in the RH and LH and, used to control the merging
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf): # iterate over length of LH and RH untilyou reach the end of i or j
            if lefthalf[i] <= righthalf[j]: # if current LH element is less than equal to current RH element
                alist[k]=lefthalf[i]    # put it in current position k and increment i (next line) so it can be compared with current RH element
                i=i+1 # increment i
            else:
                alist[k]=righthalf[j] # else if RK < LH, put RH in current position k, then increment j , so that next RH can be compared
                j=j+1
            k=k+1 # when either of the if/else conditions are met, increment k to move to next element to be filled

        while i < len(lefthalf): # will execute if we get to the end of RH from top loop
            alist[k]=lefthalf[i] # add current LH to current position k
            i=i+1  # and increment i, k and go again until condtion is false
            k=k+1

        while j < len(righthalf): # will execute if we get to the end of LH from top loop
            alist[k]=righthalf[j]  # add current RH to current position k
            j=j+1 # and increment i, k and go again until condtion is false
            k=k+1
    
# I didn't use this in the end, I coded the stable countinh sort afterwards
# Adapted from https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-10.php
#def countingSort(array1):
#    m = len(array1) # get the length of the array
#    count = [0] * m   # make an array with m elements containing 0             
    
#    for a in array1: # iterate over the array to be sorted
#        count[a] += 1    # add 1 to count array at index a. This will be done for every value a in the original array
#    i = 0 # The index for filling. Starting at zero
#    for a in range(m):    # iterate over length of array to be counted     
#        for c in range(count[a]):  # fill the array to be sorted with count[a] times value a 
#            array1[i] = a # Current index of sorted array, will be filled with a
#            i += 1 # increment i, so that next element is filled until count[a] is reached.
#    return array1 # return the sorted array

#  Adapted from https://www.cs.usfca.edu/~galles/visualization/CountingSort.html, https://courses.csail.mit.edu/6.006/spring11/rec/rec11.pdf and https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-10.php
def countingSortStable(arr1):
    #print(arr1)
    count = [0]* 100 # make a count array with enough space to count all inputs.
    for a in arr1: # Iterate of the values of arr1
        count[a] += 1 # increment count at index a by 1. This loop will count the number of times a occurs in the unsorted array.
     #print(count)

    for i in range(1,len(count)): # This loop provides stability in the sorted array
        count[i] = count[i] + count[i - 1] # The count array will now hold how many elements are <= i

    #print(count)

    result = [0] * len(arr1) # make a result array to be returned by function, same length as unsorted array
    for i in range(len(arr1),0,-1): # Iterate from end to start of arr1
        j = arr1[i - 1] # Value in arr1
        count[j] = count[j] -1 # decrement count element at index j, so we can track how many are before j after assigning j to sorted array
        res = count[j] # result of previous decrement
        result[res] = j # place j in result array at index res
    return result # return the sorted array.

# Adapted from https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheInsertionSort.html
def insertionSort(alist):
   for index in range(1,len(alist)): # Assume 1st element is sorted, so iterate from 1 to end of array

     currentvalue = alist[index] # set the current value = element at index 'index'
     position = index

     while position > 0 and alist[position - 1] > currentvalue: # This loop will compare  current position against all previous elements and swap them if current position is less than previous element, until postion is 0.
         alist[position] = alist[position - 1] # swap with previous element if loop condition met
         position = position - 1 # decrement position , so in next loop it will now be compared with previous element

     alist[position] = currentvalue # Second part of the swap (if swapping) or just assigning the same value if not swapping

# Adapted from https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheSelectionSort.html
def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1): # iterate from end of array to the start, the fillslot will move backwards from end to start of array
       positionOfMax=0 # Assume the max is at index 0 for the first comparison
       for location in range(1,fillslot + 1): #iterate from 1 fillslot + 1
           if alist[location] > alist[positionOfMax]: #if alist element at current location is > the max, assign current location to position of max
               positionOfMax = location # assign current location to position of max

       temp = alist[fillslot] # Next 3 lines swap the value of the fillslot and the max value
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

def main():   # Define the main function
    # Make a dataframe for outputting
    #cols = ['n=100','n=250','n=500','n=750','n=1000','n=1250'] # columns to be used for dataframe
    cols = ['n=100','n=250','n=500','n=750','n=1000','n=1250','n=2500','n=3750','n=5000','n=6250','n=7500','n=8750','n=10000'] # columns to be used for dataframe
    indexes = ['bubble', 'merge', 'counting', 'insertion','selection'] # row indexes to be used
    times_df =  pd.DataFrame(index=indexes,columns=cols) # make a DF to store the sorting times

    array_size = [100, 250, 500, 750, 1000, 1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000] # array with the sizes we will use for benchmarking
    #array_size = [100, 250, 500,750,1000,1250] # array with the sizes we will use for benchmarking
    
    for i in range(0,len(array_size)):  # Iterates over the different sizes of n to be sorted
        # Define a total time for each iteration of size n and each algorithm
        total_time_bubble = 0
        total_time_merge = 0
        total_time_counting = 0
        total_time_insertion = 0
        total_time_selection = 0
        print('Array Size: ', array_size[i])
        
        # calling each algorithm 10 times so an average can be calculated
        for j in range(10):
            # Create 1 array and then copy it so that each algorithm will sort a different copy of the same array, for more accurate comparison
            my_array_bubble = random_array(array_size[i]) 
            my_array_merge = list(my_array_bubble) # Make a copy of the array. Adapted from https://stackoverflow.com/a/2612815
            my_array_counting = list(my_array_bubble)
            my_array_insertion = list(my_array_bubble)
            my_array_selection = list(my_array_bubble)

            print('Run ' + str(j + 1) + ' of 10')

            # do the Bubble Sort
            #print(my_array_selection)
            start_time_bubble = time.time() # get the Start time (seconds)
            bubbleSort(my_array_bubble) # Call bubble sort function
            finish_time_bubble = time.time() # get the finish time (seconds)
            #print(my_array_selection)
            time_elapsed_bubble = (finish_time_bubble - start_time_bubble) * 1000 # Calculate time taken in ms to run the sort
            print('Time for Bubble Sort Run ', time_elapsed_bubble)
            total_time_bubble += time_elapsed_bubble # Add time taken to the running total time.

            # do the Merge Sort
            #print(my_array_merge)
            start_time_merge = time.time()
            mergeSort(my_array_merge)
            finish_time_merge = time.time()
            #print(my_array_merge)  # for checking if it sorted
            time_elapsed_merge = (finish_time_merge - start_time_merge) * 1000
            print('Time for Merge Sort Run ', time_elapsed_merge)
            total_time_merge += time_elapsed_merge

            # do the Counting Sort
            #print(my_array_counting)
            start_time_counting = time.time()
            sorted = countingSortStable(my_array_counting)
            finish_time_counting = time.time()
            #print(sorted)
            time_elapsed_counting = (finish_time_counting - start_time_counting) * 1000
            print('Time for Counting Sort Run ', time_elapsed_counting)
            total_time_counting += time_elapsed_counting

            # do the Insertion Sort
            #print(my_array_insertion)
            start_time_insertion = time.time()
            insertionSort(my_array_insertion)
            finish_time_insertion = time.time()
            #print(my_array_insertion)
            time_elapsed_insertion = (finish_time_insertion - start_time_insertion) * 1000
            print('Time for Insertion Sort Run ', time_elapsed_insertion)
            total_time_insertion += time_elapsed_insertion

            # do the Selection Sort
            #print(my_array_selection)
            start_time_selection = time.time()
            selectionSort(my_array_selection)
            finish_time_selection = time.time()
            #print(my_array_selection)
            time_elapsed_selection = (finish_time_selection - start_time_selection) * 1000
            print('Time for Selection Sort Run ', time_elapsed_selection)
            total_time_selection += time_elapsed_selection

        print('Bubble Sort Total time: ', total_time_bubble) # for checking everything is as expected
        print('Merge Sort Total time: ', total_time_merge)
        print('Counting Sort Total time: ', total_time_counting)
        print('Insertion Sort Total time: ', total_time_insertion)
        print('Selection Sort Total time: ', total_time_selection)
    
        #times_df.iat[0,i] = round((total_time_bubble/10),3) # Add average, rounded to 3 places, bubble sort times to first row of dataframe
        #times_df.iat[1,i] = round((total_time_merge/10),3)  # Add merge sort times to second row of dataframe
        #times_df.iat[2,i] = round((total_time_counting/10),3) # Add counting sort ...
        #times_df.iat[3,i] = round((total_time_insertion/10),3) # Add insertion sort ...
        #times_df.iat[4,i] = round((total_time_selection/10),3) # Add selection sort ...

        times_df.iat[0,i] = total_time_bubble/10 # Add average, rounded to 3 places, bubble sort times to first row of dataframe
        times_df.iat[1,i] = total_time_merge/10  # Add merge sort times to second row of dataframe
        times_df.iat[2,i] = total_time_counting/10 # Add counting sort ...
        times_df.iat[3,i] = total_time_insertion/10 # Add insertion sort ...
        times_df.iat[4,i] = total_time_selection/10 # Add selection sort ...

        print('Bubble Sort Avg: ', times_df.iat[0,i]) # for checking everything is as expected
        print('Merge Sort Avg: ', times_df.iat[1,i])
        print('Counting Sort Avg: ', times_df.iat[2,i])
        print('Insertion Sort Avg: ', times_df.iat[3,i])
        print('Selection Sort Avg: ', times_df.iat[4,i])

    times_df['n=100'] = times_df['n=100'].astype(float) # Rounding wasnt working because columns were objects. Recasting them as floats
    times_df['n=250'] = times_df['n=250'].astype(float)
    times_df['n=500'] = times_df['n=500'].astype(float)
    times_df['n=750'] = times_df['n=750'].astype(float)
    times_df['n=1000'] = times_df['n=1000'].astype(float)
    times_df['n=1250'] = times_df['n=1250'].astype(float)
    times_df['n=2500'] = times_df['n=2500'].astype(float)
    times_df['n=3750'] = times_df['n=3750'].astype(float)
    times_df['n=5000'] = times_df['n=5000'].astype(float)
    times_df['n=6250'] = times_df['n=6250'].astype(float)
    times_df['n=7500'] = times_df['n=7500'].astype(float)
    times_df['n=8750'] = times_df['n=8750'].astype(float)
    times_df['n=10000'] = times_df['n=10000'].astype(float)
    
    times_df = times_df.round(3)
    # Adapted from https://stackoverflow.com/a/31885295
    print(tabulate(times_df, headers='keys', tablefmt='grid'))  # Print a table, use columns as headers, format in grid style
    


if __name__ == "__main__":
    main()

