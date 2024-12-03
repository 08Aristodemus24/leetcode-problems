

def maxProduct(nums):
    length=len(nums)
    nums=sorted(nums,key=abs)
    return nums[length-1]*nums[length-2]*nums[length-3]
 
# given array of length 3 until 10^4
# multiply three numbers by each other such that its product is the maximum out of all products
# of the other numbers

# method 1:
# length case 
# 3: multiply all numbers anyway since product of the three has the max
# more than 3 find the 

def main():
    nums=[-1,-2,1,2,3]
    nums=sorted(nums,key=abs)
    print(nums)

main()