
    # length cases
    # 0 return
    # 1 with or without zero return
    # 2 or more [0,1,0,3,12]

    # do it without copying any data in array
    # runs at O(n)
    # may use insert or remove functions since both run at O(n) implement only when necessary
    
    # method 1: 
    # remove all zeroes first using loop
    # determine count of zeroes
    # append all zeroes at the end based on count

def moveZeroes(arr):
    length=len(arr)
    if length==1 or length==0:
        return
    else:
        count=0
        i=0
        i=0
        while i<length: # break out of loop such that zeroes are all gone
            if arr[i]==0:
                arr.remove(arr[i])
                arr.append(0)
            i+=1 # increment i only if there is no zero encountered
                
            

def main():
    arr=[0,0,3]
    arr1=[0,1]
    moveZeroes(arr)
    moveZeroes(arr1)
    print(arr)
    print(arr1)

main()