def numrot(nrot,length):
    num=0
    while num<=nrot:
        num+=length

    num=num-length
    nrot=nrot-num
    return nrot

def leftrotate(arr,nrot):
    nrot=numrot(nrot,len(arr)) # optimize number of rotations
    inn=len(arr)-nrot

    if len(arr)==0 or len(arr)==1 or nrot==len(arr):
        return

    else:
        temp=[]
        for i in range(0,nrot,+1): # save out of bound elements in temp array
            temp.insert(i,arr[i])

        for i in range(0,inn,+1):
            arr[i]=arr[i+nrot]

        i=inn 
        j=0
        while j<nrot:
            arr[i]=temp[j]
            j+=1
            i+=1
        
    print(arr)

def main():
    arr=[1,2,3,4,5,6,7,8,9,10]
    leftrotate(arr,10)
    
main()