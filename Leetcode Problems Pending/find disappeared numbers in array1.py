def findMax(nums):
    length=len(nums)
    cur_max=nums[0]
    i=1
    while i<length:
        if cur_max<nums[i]:
            cur_max=nums[i]
        i+=1
    return cur_max

def findDisappearedNum(nums):
    cur_max=findMax(nums)
    nums.sort()
    print(nums)
    length=len(nums)
    count=1
    temp=[]
    while count<length:
        if count!=nums[count-1]: 
            temp.append(count)
        count+=1
            
    return temp

# [1,3,5,2,7,8,10]
# array is from 1 to n inclusive

# method 1: unsorted 
# since n is inclusive theory is to subtract n from the max num of the array
# 10 is the max but n/length of array is 8
# 
# max num cases:
# max is <= length [1,3,5,2,3,2,6,7] 
# - for this case max can either be < or = to the length
# - all other elements lie within the range of n/length to 0 range exclusive
#
# length cases:
# 1 and max <= length just return since there is no other element return
# 2 max < length [6,1,2,2,4,5,6,6]
# count number of occurences first for each number first
# all other numbers greater than it is missing add max+1 max+2 < length-max only 
# 
# 2 max == length [6,6,6,6,6,6] [1,2,2,3,3,6]
# all other disapperead number is in range 
#


# 1. first is find the max
# 2. compare max to length
# 3. 

# method 2: using count from 1 to n 
# idea is to loop from 1 to n using count and see if each element is equal to count
# [1,2,3,4,5,6]
# [1,2,2,3,4,4]

# method 3: sorted

def main():
    arr=[4,3,2,7,8,2,3,1]
    print(findDisappearedNum(arr))

main()