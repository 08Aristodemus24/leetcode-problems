def findNextMin(nums):
    length=len(nums)
    if length==1: # if length is 1 there is no possibility of finding the next minimum
        return nums[0]

    cur_min=nums[0]
    for i in range(1,length): # find the first min
        if nums[i]<cur_min:
            cur_min=nums[i]
    ptr=
    for i in range(1,length):
        if ptr!=cur_min and ptr>nums[i]: # if a certain element is found that meets these two conditions then update ptr
            ptr=nums[i] # next min must not equal first min but greater than it and lesser than all other elements except for first min
    return ptr
        
def Main():
    nums=[5,6,7,8] # 5 is the minimum find the next larger element than it
    print(findNextMin(nums))

Main()

