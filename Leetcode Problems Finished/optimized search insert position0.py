# time complexity: unknown

def Rbsearch(arr,key,lo,hi):
    if lo>hi: # if lo > hi that means that element being searched is not found
        return -1
    else:
        mid=int((lo+hi)/2)
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            return Rbsearch(arr,key,lo,mid-1)
        else:
            return Rbsearch(arr,key,mid+1,hi)
    

def modRbsearch(arr,lo,hi,target):
    mid=int((lo+hi)/2)

    # 1,2,3,5,6,7,8 insert 4 
    # find the spot where target is in between maximum number less than target and minimum number greater than target
    if arr[mid]<target and arr[mid+1]>target: # there is only one point that the target can insert itself
        return mid
    elif arr[mid]>target:
        return modRbsearch(arr,lo,mid-1,target)
    else:
        return modRbsearch(arr,mid+1,hi,target)

def findpos(arr,key):
    if arr[0]<key<arr[len(arr)-1]: 
        pos=modRbsearch(arr,0,len(arr)-1,key)
        arr.insert(pos+1,key)
        return arr.index(key)
    elif key<arr[0]:
        arr.insert(0,key)
        return 0
    else:
        arr.append(key)
        return arr.index(key)
    
class Solution:
    def searchInsert(self,nums,target):
        check=Rbsearch(nums,target,0,len(nums)-1)
        if check!=-1:
            return check
        else: # if element is not present insert target into nums
            return findpos(nums,target)

def main():
    arr=[1,2,3,5,6,7,8,9,10]
    event=Solution()
    #print("position of inserted num is "+"["+str(findpos(arr,4))+"]")
    print(modRbsearch(arr,0,len(arr)-1,10))
    
    

main()