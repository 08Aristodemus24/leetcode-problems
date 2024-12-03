from random import randint

def mergesort(arr,lo,hi):
    mid=int(lo+hi/2)+1
    if lo>=hi: # range value or base case is when the array length reaches 1
        return
    t_left=arr[:mid] # assign left most elements in mid in temp array, 0 < mid
    t_right=arr[mid:] # assign right most elements in mid in temp array, mid < length

    mergesort(t_left,lo,mid-1) # process the left side first, pass in the arr that is already halved such that in recursive calls it gets smaller everytime
    mergesort(t_right,lo,hi-mid) # process right side second, pass the new lo and hi of each array
    
    i=j=k=0
    while i!=mid and j!=hi-mid+1:
        if t_left[i]>t_right[j]: # arr is only modified for the specific temp array passed  
            arr[k]=t_right[j] # note that real arr will not be modified until last recursive call has been executed
            j+=1
        else:
            arr[k]=t_left[i]
            i+=1
        k+=1
    if j!=hi-mid+1: # if j or i pointers have still elements left append those remaining elements 
        for j in range(j,hi-mid+1):
            arr[k]=t_right[j]
            k+=1
    else:
        for i in range(i,mid):
            arr[k]=t_left[i]
            k+=1
        
def main():
    arr=[]
    for i in range(100):
        arr.append(randint(0,100))
    mergesort(arr,0,len(arr)-1)
    print(arr)

main()
    