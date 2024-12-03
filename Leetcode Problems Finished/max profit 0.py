

def maxProfit(nums):
    length=len(nums)
    i=1
    maxP=0
    if length==0 or length==1:
        return maxP
    cur_min=nums[0]
    while i<length:
        if cur_min>nums[i]:
            cur_min=nums[i]
        else:
            temp=nums[i]-cur_min
            if maxP==None:
                maxP=temp
            elif maxP<temp:
                maxP=temp
        i+=1
    return maxP

# [7,1,5,3,6,4]
# ith element is the price of a given stock on day i ex. buy on day 2 which is the day-1th index==1
# sell on day 5 which is day-1 index==6
# price for selling day - price for buying day = 5
# 
# -note that all previous elements of buying element must not be touched since you have to buy firsy
# -and all elements that needs to be bought first before selling must be not greater or equal the selling price
# 7 > 1 so 1-7 cannot work since it would be negative or zero if ever selling and buying is equal 
# 1 < 5 so 5-1=4

# array is in random permutation
# there is no backward functionality meaning you cannot buy one day and sell the previous day
# you cannot sell stock before you buy


# method 3: linear scan with updating min every single time
# find the first cur min and set to first elem
# if next elem is greater than or equal do the necessary operations and keep it inside maxP
# else found a next cur min which is the selling elem
# update cur min 
# and repeat process of finding the maxP
# keep updating maxP until the end

# length cases
# if 1 return max which is 0
# 2 check if elem

def Main():
    nums=[7,1,5,3,4,0,7]
    print(maxProfit(nums))

Main()