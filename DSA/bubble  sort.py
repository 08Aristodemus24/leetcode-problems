
def bubblesort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if(arr[j]>arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp

def mergesort(arr):
    pass

def quicksort(arr):
    pass

def main():
    arr=[2,10,4,6,7,1,8,9,5,3]
    bubblesort(arr) # array is modified because array is mutable
    print(arr)


main()
