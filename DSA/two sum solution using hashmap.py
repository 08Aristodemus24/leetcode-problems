class Solution:
    def findTwoSum(self,nums,target):
        keys={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if keys.get(diff) is not None:
                return [keys[diff],i]
            keys[nums[i]]=i
                

if __name__ == "__main__":
    event=Solution()
    x=event.findTwoSum([2,-5,14,9],9)
    print(x) 

# problem:
# given an array of nums [2,7,11,15]
# and a target 9
# find the indeces that add up to the target
# 2 and 7 add up to 9

# method:
# loop through the array starting from 0 to length
# ex. at 2, get the subtrahend of the of the two
# by getting the abs diff of the target 9 and cur num 2
# 9-2=7 search in hashmap
# if no value exists add seven to the 

# idea:

# figure out:

# cases/samples: