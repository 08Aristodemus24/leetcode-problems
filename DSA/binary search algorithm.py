
def rbsearch(arr,key,lo,hi):
    print()

def bubblesort(arr,length):
    for i in range(length-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp

arr=[2,5,10,29,32,23,5,1,6]
bubblesort(arr,len(arr))
print(arr)



