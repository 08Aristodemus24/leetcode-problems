def compare(arr):
    length=len(arr)
    i=1
    curmax=arr[0]
    while i<length:
        if curmax<arr[i]:
            curmax=arr[i]
        i+=1
    return curmax

def maxSubArray(nums):
    sum=0
    sums=[]
    if len(nums)==0:
        return # return single value since nums may contain either just one or none
    
    elif len(nums)==1:
        return nums[0]
    
    else:
        for num in nums:
            if sum+num<0:
                sum=0 # reset value of sum 
                sums.append(num) # still append negative element because take in consideration what if list was all neg vals
            else:
                sum+=num
                sums.append(sum)
    
    return compare(sums)

def main():
    arr=[-2,-5]
    max=maxSubArray(arr)
    print(max)
main()
