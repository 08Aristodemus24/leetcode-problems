from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # initialize empty hashtable
        # key is complement, and value is current value in loop
        comp_curr = {}
        n = len(nums)

        for i in range(n):
            # target - current number to get complement
            curr = nums[i]
            comp = target - curr
            print(comp)

            # if key is non existent add key after this if since
            # nums[i] in comp_curr will be false
            if curr in comp_curr and curr + nums[comp_curr[curr]] == target:
                return [i, comp_curr[curr]]

            # add first key and value comp and i of curr in comp_curr    
            comp_curr[comp] = i

        print(comp_curr)