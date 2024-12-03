nums=[1,1]

length=len(nums)

i=0
while i<length-1: # no need to loop until last element
    while True:
        if nums[i]!=nums[i+1]: # keep looping until next element is 
            break
        elif i!=length-2: # check if index is at second to the last element
            nums.pop(i)
        else:
            nums.pop(i)
            break           
        length=len(nums)# update length
    i+=1

print(nums)