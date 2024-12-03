def Lsearch(nums,key):
    for i in range(len(arr)):
        if nums[i]==key:
            return i
    return -1

class Solution():
    def twoSum(self, nums, target):
        # no need to check if the sum of every element is equal to the target
        list=[]
        for i in range(len(nums)):
            sub_tra=target-nums[i]
            j=Lsearch(nums,sub_tra)
            if j!=-1 and j!=i and sub_tra+nums[i]==target:
                list.append(i)
                list.append(j)
                break
                        
        return list



arr=[1,2,3,4,5,6,7]