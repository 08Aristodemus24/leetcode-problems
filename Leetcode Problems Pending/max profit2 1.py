def maxProfit(nums):
    length=len(arr)
    hi=length-1
    for i in range(hi,-1,-1):


# like the first problem we know that buying must also be before selling
# and buying price must be greater than selling
# we keep track of the buying price and see if 
# buying price is > than selling price
# else set buying price as new minimum
# everytime it is subtracted by selling price update current max profit
# if found a new minimum update minimum buying price and see if next coming days
# selling price - buying price is greater than current max profit

# method 1: linear time update min and max profit start at the beginning of the array
# [7,1,5,3,6,4] negative is non-existent
# cur min is 1 and next element is 5
# 5-1 is 4 update maxp from 0 to 4
# check every time if found a min element lesser than current min


# method 2: linear time but start at the end of the array
# [7,1,5,3,6,4]
# start scan at length-2 or hi-1
# compare if min<num[hi]
# if yes subtract and upddate current max
# check if that difference is greater than current max
# if yes update
# no move to next number/
#
# else move on to the next number/dont do anything

# always check if current min is lesser than the 