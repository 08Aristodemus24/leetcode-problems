# given array [1,2,3]
# find the third maximum number and return it
# third maximum number can be defined as
# maximum number>2nd max number>3rd max number
# 2nd max is defined as the largest element in the array that is also < max number

# method 1: sort array return index [length-3] or sort array in descending order return index [2]

# method 2: find max number first, then find 2nd max number using max, lastly find 3rd max using 2nd max 

# method 3: 
def thirdMax(nums):
    length=len(nums)
    nums.sort()
    cur_max=nums[length-1] # this is the max number
    count=1
        
    if length==1 or length==2: # there is no possibility of third number in array
            return cur_max

    ptr=cur_max
    # find second max here
    for i in range(length-2,-1,-1):
        if ptr>nums[i] and count!=3: # trying to find a specific max which in this case is the third max
            ptr=nums[i]
            count+=1 # this will detect if for every number less than cur_max it will know what specific max number that is
                    
    if count==3:
        return ptr # return found 3rd element
                    
    return cur_max # return current max if no third element id found
        

def main():


main()