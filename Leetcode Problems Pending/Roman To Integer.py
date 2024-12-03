class RomanNumeral:
    def romanToInt(self,rom_num:str)->int:
        keys={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        i=0
        sums=0
        prev=0 # initially zero since there is no previous value to compare with the first roman numeral
        while i<len(rom_num):
            if keys[rom_num[i]]>prev:
                sums=sums+(keys[rom_num[i]]-prev)
                i+=2
                prev=keys[rom_num[i-1]]
            else:
                sums=sums+prev
                prev=keys[rom_num[i]]
                i+=1
                
        return sums # when string length is 0 it returns a sum of 0
        


def Main():
    event=RomanNumeral()
    print(event.romanToInt("IV"))

Main()

# since all every character is different have an array of characters
# of roman numerals
# do a linear scan from left to right and identify the different characters
# a linear scan will do since it is a string

# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# ex. IV since I is 1 and V is 5 we know that I has a lesser precedence than the V
# so we convert I first to 1 and V to 5 then get the abs value of 1 and 5

# Phase 1: Conversion of one character
# for III, VI
# we convert each character to its respective digit and add them
# for III we see 3 characters
# to set this up in linear time we set up a count to count the occurences of these values
# and depending on its value
# we use the count*the right value for the roman numeral
# I is 1 and we count 3 therefore 1*3=3
# 
# VI for this example
# we see V as 5 and I as 1
# since count of V is 1
# 5*1=5
# and for I 
# 1*1=1
# once another character is encountered start the count again
# once count is done add both numbers
# this is done by maintaining a sum variable
# once another is found update sum=0 by adding the product of the characters 

# Phase 2: Checking if it is nearing next character
# IV is next V
# IX is next to X
# XL is next L
# XC is next to C

# I is 1 and V is 5
# we need to check everytime if precedence of i is lesser than i+1
# if not then just count then add
# else subtract

# I is 1 and X is 10
# I has a lower precedence than X 
# therefore subtract

# XLIX
# X is lesser than L 
# X is 10 and L is 50 therefore subtract
# sum is now 40
# but as we can see I is less than X so we cannot
# directly add the current sum to I
# we need to suybtract I to X first which is 1-10
# which is 9 then add 40
# which is 49
# to eliminate this problem once the calculation has been done
# move pointer to next value
# XLIX
# ^
# pointer at X
# gets value of X and gets value of the roman beside it
# checks if pointer is < next value


# XCIV
# X is lesser than C which are 10 and 100 which makes 90
# I is lesser than V which are 1 and 5 which makes 4
# add 90 and 4 = 94
# 

# note you do not need a count variable to count all the occurences
# a linear scan which gets all the values and adds them to the sum is sufficient
# CCXXIV
# ^
# gets value of pointer and next
# checks if pointer < next
# no so C is added to sum
# move pointer

# pointer < next
# no so C is added to current sum
# move pointer

# X < X
# no so X is added to current sum
# move pointer

# X < I
# no so X is added to current sum
# move pointer

# I < V
# yes do calculations
# move pointer such that next is skipped
# case 1: once i is moved and skipped i will be greater than range
# solution: use while loop to check if i >= range if not i is still < range 

# Phase 3: Checking it it is the next character
