class Solution:
    def revSentenceStrings(self,sen:str)->str:
        sen=list(sen)
        length=len(sen)
        result=""
        i,lo=0,0
        while i<length-1:
            if sen[i+1]==' ':
                hi=i
                self.reverse(sen,lo,hi) # string is a list
                lo=i+2 # lo pointer skips the white space and goes to new char
                i=lo # i ptr is set to new char
            elif i+1==length-1: # this is to check the case if string has no white space which is nearing end
                hi=i+1
                self.reverse(sen,lo,hi) # low is already set in previous string or initially set to 0
                i+=1
            else:
                i+=1
        return "".join(sen)

    def reverse(self,string,lo,hi)->list:
        if lo>=hi:
            return
        string[lo],string[hi]=string[hi],string[lo]
        self.reverse(string,lo+1,hi-1)


def Main():
    event=Solution()
    result=event.revSentenceStrings("hello my name is larry miguel cueva")
    print(result)

Main()
# problem:
# given a sentence with strings
# reverse each string in the sentence such that only strings
# are reversed 
# and the spaces are preserved

# method:
#

# idea:
# -since each string is separated by white spaces we must
# check ahead of time if there are white spaces
# -either by starting at the end or at the front
# 
# -once string is detected by white space we reverse that string recursively
# -getting and using its lo and hi indeces
# -once the string is reversed we place each character in an empty string, starting at the
# first string
# -to get the lo and hi indeces find the length first
# -once whitespace is detected we get the current i value and set it as the new hi
# -when new character is detected we set its index as the new lo index and once whitespace is detected
# we set it as the new high
# -convert string to list so that reverse does not use extra space

# cases:
# 1. sentence with no whitespace or a single string
# have a while loop that handles strings with no white space
# -single chars
# -2 or more chars
#
# 2. sentence has whitespace
# do the necessary calculations for it

# figure out:
# how do we insert the reversed characters in an empty string? STRING CONCATENATION
# how do we know if the sentence is just one one string?
# if pointer reaches end without any whitespace then that means we use the last
# i value - 1 since we already reached the end

# samples:
# "hello"
# no whitespace detected lo is 0 and hi is 4
# reverse indeces
#
# "hello world"
#  ^   ^
# lo is initially 0
# once pointer reaches o it detects a white space
# the hi is set as the current i value then reversal takes place
# i skips the white space and is met with a new charater 
# lo is currently at w and once i reaches the last char set it as the new hi