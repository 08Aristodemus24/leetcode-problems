class Solution:
    def addBinary(self,a:str,b:str)->str: # return the sum of both the strings
        pass



# problem:
# we know that digits go only up to 0 and 1 and if sum of binary digit exceeds
# 1 we subtract it by the maximum digit of a binary number
#
# similar to adding decimal numbers adding 19 and 8 for example
# 19
#  8
# 9+8 is 17 since 17 exceeds the maximum digit we split 17 carry the first digit and
# add it to the next digit
# or we use the base of a decimal which is 10 and minus 17 by 10 and carry the first digit

# in the case of binary numbers if it exceeds the maximum number 1 we subtract
# it by its base which is 2 and carry the one
# 101
#  11
#   ^ 1+1=2 minus 2 to get the real value
# and to get the carry value we divide the sum by the base which is 2/2=1 which will be the carry
# if this were to be 1 we divide it by base 2 and the carry will still be zero since 1 does not exceed max
# 

# methods:
# 

# ideas:
# start with the first digit of the 1st binary number and first digit of the 2nd binary number
# consider the case of either one of the strings have greater length than the other
# if one of their pointers reaches the end break out of loop
# use i and j
# start from length down to 0
# 10011
#   101
# last carry before j pointer exceeds range is 1
# so 1+1=2
# but 2 > 1 so 2-2=0 and carry=sumval/2
# loop only from remaining values of i


# by then carry value should be updated to act on the rest of the rest of the digits of the larger string
# add carry value to the digit
# if sumval > base-1(1) then sumval-=2 and carry=sumval/2
# move to the rest of the digit and do the process again


# cases:
# 1. 1+1    two digits
# 2. 10...+1    str1 has 2 or more digits and str2 has 1 digit and vice versa


# figure out:

# samples:
# 19
# 19
# 19
# 9+9+9=27-10=17-10=7 this is the final sum value since 7<=9
# 27/10=2 this is the final carry value 
# 2+1+1+1=5 this is the final sum value since 5<=9

# note if sum val exceeds base-1 then subtract by base sumval>base-1
# 101
# 111
# 011
# 1+1+1=3-2=1 this is the final sum value since 1<=1
# 3/2=1 this is the final carry value
# 1+1+1=3-2=1 this is the final sum value since 1<=1
# 3/2=1 this is the final carry value
# 1+1+1=3-2=1 this is the final sum value since 1<=1
# 3/2=1 this is the final carry value
# since nothing to add bring down carry value
# 1111