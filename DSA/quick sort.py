from random import randint

def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]

def partition(arr,lo,hi):
    pivot=randint(lo,hi)
    swap(arr,pivot,hi) # swap last element in pivot element
    i=lo 
    j=hi-1 # set j pointer to the last end of the scan
    
    while i<=j: # when i pointer has greater index it has crossed the border of the j pointer
        if arr[i]>=arr[hi]>arr[j]: # if i and j ptrs are < and >= to pivot swap then inc & dec
            swap(arr,i,j)
            i+=1
            j-=1
        
        # check if either of the two needs to be incremented or decremented or both
        elif arr[i]>=arr[hi]<=arr[j]:
            j-=1
        elif arr[j]<arr[hi]>arr[i]:
            i+=1
        else:
            i+=1
            j-=1
    swap(arr,i,hi) # swap pivot element located in [hi] and swap with i
    return i # return new position of fixed pivot element

def quicksort(arr,lo,hi):
    if lo<hi: # if lo is greater than or equal hi, means array length reached 1
        fixed=partition(arr,lo,hi)
        quicksort(arr,lo,fixed-1) # process sorted left side of pivot
        quicksort(arr,fixed+1,hi) # process sorted right side of pivot

        
def Main():
    arr=[]
    for _ in range(20):
        arr.append(randint(0,50))
    quicksort(arr,0,len(arr)-1)
    print(arr)
Main()


# quicksort(arr,new lo,new hi) left side
        # quicksort(arr,new lo,new hi) right side

# pick a pivot element randomly using a rand function
# place all other elements greater than or equal to the pivot on the right
# and place all other elements lesser to the pivot on the left

# pick a pivot again on the left side and place all respective elements

# phase 1: pivoting
# use rand function to generate a random index from 0 to length exlusive
# once picked switch out last element to the value of that index
# use pointers i and j to access each value of all the elements that need to be sorted on both right and left sides
# i will look for the value >= to the pivot
# j will look for the value < the pivot
# 
# conditions:
# if i finds a >= value than pivot fix that index
# j finds a < value than pivot fix that index and swap i and j
# else keep moving i until value is >= pivot
# also keep moving j until value is < pivot

# [5,4,3,6,2,8,13,9,10,2,4] 11 elements
# chosen pivot [i=7]
# [5,4,3,6,2,8,13,4,10,2,9] switch 4 and 9
# [5,4,3,6,2,8,2,4,10,13,9]
# [5,4,3,6,2,8,2,4,9,13,10] 
#
# start i at [0] and start j at [length-2] or [hi-1]
# 2 is found by j but i hasnt yet so move i inwards
# 13 is found by i so swap 2 and 13
# move i and j inwards 
# i reaches 10 and j reaches 4 but we see that i index is already greater than j so we stop
# we use the ith index of that last pointed element to swap with the pivot
# 9 is already sorted in that position so we only need to use the left and right portions of it
# 0 to last index value of i exlusive for left
# i+1 to length/hi+1

# [5,4,3,2,8,2,4] lo 0 hi 6
# chosen pivot [i=2] switch 4 and 3
# [5,4,4,2,8,2,3] found 5 for i found 2 for j so swap
#  ^         ^ 
# [2,4,4,2,8,5,3] found 4 for i found 2 for j so swap
#    ^   ^
# [2,2,4,4,8,5,3] found 4 again for i found 2 for j but i > j so stop
#    ^ ^
# switch 3 and 4

# [2,2] lo 0 hi 1
# chosen pivot [i=1] switch last with pivot [i]=last, last=[i]
# [2,2] found 2 for i but j has gone out of bounds but still i > j so stop
#  ^ ^
# switch 2 and 2

# [2] lo 0 hi 0 
# when lo and hi is equal stop recursion and return
