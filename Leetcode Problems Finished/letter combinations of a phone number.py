class Solution:
    def letterCombinatorics(self,digits:str)->list:
        return self.buildCombinations(digits,"",0)

    def buildCombinations(self,digits:str,cur_letter:str,index:int)->list:
        keys={
            "2":['a','b','c'],
            "3":['d','e','f'],
            "4":['g','h','i'],
            "5":['j','k','l'],
            "6":['m','n','o'],
            "7":['p','q','r','s'],
            "8":['t','u','v'],
            "9":['w','x','y','z']
        }

        result=[]
        hi=len(digits)-1
        
        if index>hi:
            return cur_letter
        
        for i in keys[digits[index]]: # pass in the keys of the digit of the current index
            result.extend(self.buildCombinations(digits,i,index+1)) # when last digit is reached in string letters of that digit is passed and then returned again to be put inside list
            # "p" "q" "r" "s" is returned then put inside list

        for i in range(len(result)): # current letter is currently the digit that came before the passed digits letters above 
            result[i]=cur_letter+result[i] # ["d"+"p", "d"+"q"......]
 
        return result # return the built list of strings

def Main():
    combinations=Solution()
    print(combinations.letterCombinatorics("239"))
        



Main()

# problem:
# given digits 2-9
# return all possible letters that each digit in the entered number has
# e.g. 29
# 2 has letters abc
# 9 has letters xyz
# note that each letter used is only repeated ONCE
# ax,ay,az,
# and letteres of the digit cannot be paired to its letters
# aa cannot be, ab cannot be
# zy cannot be
# we map each digit to each of the next digits letters 
# 234 for example 2 has abc, 3 has def, and 4 has hij
# adh,adi,adj
# as we can see, we can clearly see a pattern being made
# a and d already has a path to it and next path is g
# 1st combination is made then we go back to a then d then g
# but as we can see g has already been visited previously and is already
# a combination made so we go to d and make a decision again but this time
# we choose h so we make the path adh
# so far we have made the combinations adg and adh
# we make the same process and start from a then d then i
# and make the path adi
# to visualize the problem further
# we draw a matrix that represents each digits letters 
# a d g
# b e h
# c f i

# method:


# idea:
# -to do this backtrack algorithm we must have a count variable that represents how many visits we have
# left in that specific number and its letters
# for ex. 3 has letters def
# we have 3 visits
# d is visited
# -another idea can be to keep track of all the chars we have visited in that specific digit
# if we have visited that char we must check in our temporary set of visited chars
# to see if we have already visited that specific chars

# figure out:
# how do we keep track of the paths when each function there will be a new empty list? pass in the paths every single time
# how do we know when to stop 

# cases:

# samples:
