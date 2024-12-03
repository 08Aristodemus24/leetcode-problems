def findUnsortedsSubArray(nums):
    pass

# input size is from 1 - 10000
# what needs to be found is the ff:
# shortest subarray
# that is unsorted
# and continuous such that when sorted it will connect its first and last elements to the untouched
# adjcacent elements of the array
# [2,6,4,8,10,9,15]
#    ^        ^
# untouched adjacent elements of the array is 2 and 15
#
# [1,1,5,1,3,8,6,10,10]
#      ^       ^
# UA elements of the array is 1 and 10 with elements adjacent and the same as the UA element
# 
# [0,1,4,1,4,5,6]
#      ^ ^
# UA elements of the array is 1 and 4 s
# 
# first element of the continuous array can be the first element detected to be greater than the untouched element
# and also lesser than the other untouched element

# length cases
# if 1 return 1
# if 2