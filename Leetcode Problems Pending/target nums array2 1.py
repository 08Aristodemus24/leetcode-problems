def Rbsearch(nums,key,lo,hi):
    if lo>hi:
        return -1
    else:
        mid=int((lo+hi)/2)
        if nums[mid]==key:
            return mid
        elif nums[mid]<key:
            return Rbsearch(nums,key,mid+1,hi)
        else:
            return Rbsearch(nums,key,lo,mid-1)

def Lsearch(nums,key):
    for i in range(len(arr)):
        if nums[i]==key:
            return i
    return -1

def twoSum(nums,key):
    res=[]
    for i in range(len(nums)):
        sub=key-nums[i]
        j=Rbsearch(nums,sub,0,len(nums)-1)
        k=Lsearch(nums,sub)
        if i<j and i!=j and nums[j]+nums[i]==key:
            res.append(i+1)
            res.append(j+1)
            break
        elif nums[i]==sub and nums[k+1]+nums[i]==key:
            res.append(i+1)
            res.append(k+2)
            break
    return res
    # since array is sorted do binary search on the subtrahend of the current minuend
    # subtract target from minuend and see if that result exists in the array
    # if yes
    # check if i<index returned and i!=index returned 
    # yes return place i and index returned in result array
    # no move to next element
    
    # what if there are duplicates in the array
    # we know that if key-nums[i] it will produce the subtra which will be searched
    # if subtra and nums[i]== we will have to do a possible linear search


def Main():
    arr=[1,2,3,4,4,9,56,90]
    print(twoSum(arr,8))

Main()