from random import*

def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp

def partition(arr,lo,hi):
    pivot=randint(lo,hi)
    print(arr[pivot])
    swap(arr,pivot,hi) # swap last element in pivot element
    i=0 
    j=hi-1 # set j pointer to the last end of the scan
    
    while i<=j:
        if arr[i]>=arr[hi] and arr[hi]>arr[j]: # if i and j ptrs are < and >= to pivot swap then inc & dec
            swap(arr,i,j)
            i+=1
            j-=1
        else:
            # check if either of the two needs to be incremented or decremented or both
            if arr[j]>=arr[hi] and arr[i]>=arr[hi]:
                j-=1
            elif arr[i]<arr[hi] and arr[j]<arr[hi]:
                i+=1
            else:
                i+=1
                j-=1
    swap(arr,i,hi) # swap pivot element located in [hi] and swap with i
    print(i)


def Main():
    arr=[8,9,6,7,10,5,1,3,4,2]
    partition(arr,0,len(arr)-1)
    print(arr)

Main()