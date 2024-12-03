class Solution:
    def reformat(self,s:str)->str:
        nums=0
        letters=0
        for i in s:
            if 'a'<=i<='z':
                letters+=1
            else:
                nums+=1
        diff=nums-letters
        if diff==0 or diff==1:
            pass
        else:
            pass
        return ""

# given an alphanumeric string (string containing numbers and lowercase letters)

# problem:

# method:
# in checking if one character use a loop that will not execute
# set two counts one for number of letters and one for number of digits
# once diff hits any of the numbers then we do the operations

# idea:
# only format string if it contains both letters and characters
# use isdigit() to check if string contains only digits
# use isalpha() to check if string contains only letters
# if one of them is false
# isdigit(T) and isalpha(F) ,vice versa, or both false then return empty string
# if count of digits - count letters either 0,1,-1 
# if 0 then that means digits and letters have the same count
# if 1 then that means digits is greater than letters by one digit
# if -1 then that measn number of letter is greater than numbers by one digit
# if difference doesnt hit anything then retrun an empty string
# 
# operation in formatting
# if number of digits is >= than number of letters then 
# digits must come first
#
# else then letters must come first
#
# a0b1c2 letters and digits equal therefore digits come first
# find numeric character first 


# cases:
# 1. empty string return empty string
# 2. 1 character return empty string
# 3. 2 or more characters then reformat
# 
# 2 or more character subcases:
# 1. what if number of digits is not the same with number of letters
# 2. what if number of letters is not the same witn number of digits
# 

# to figure out:
# find permutation such that all letters and number are alternating
# how to put number first then letter then number then letter and so on..
