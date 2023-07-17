from typing import *

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # normalize number of rotations first
        k = k % n

        # allocate empty list
        rotated = [0] * n

        for i in range(n):
            # calculate next position
            next = (i + k) % n
            rotated[next] = nums[i]

        nums[:] = rotated[:]
