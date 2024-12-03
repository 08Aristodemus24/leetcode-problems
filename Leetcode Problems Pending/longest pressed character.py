class Solution:
    def isLongPressed(self,name:str,typed:str)->bool:
        seq=[]
        count=0
        ptr=name[0]
        for i in name:
            if ptr!=i:
               seq.append(count)
               count=1
               ptr=i
            else:
                count+=1
        seq.append(count)
        
        j=0
        count=0
        ptr=typed[0]
        for i in typed:
            if ptr!=i and count>=seq[j]: # check if character has reached another character 
                count=1
                ptr=i
                j+=1
            elif ptr!=i and count<seq[j]: # when count is greater than sequence of one character then 
                return False
            else:
                count+=1
        return True

def Main():
    string="laarrryyy"
    event=Solution()
    print(event.isLongPressed(string,"larrryyy"))

Main()
# problem:
# given a name
# determine if either one or more characters is long pressed
# larry -> laarrryyy
# return true if characters have been long pressed
# if and only if each character has been pressed equal to the length of that character in the name or greater
# ll pressed 2 times which is > than l which is 1
# y pressed 1 time which is == to y which is 1
# condition must be <= for how many times the character was pressed

# methods:
# 1: run this in linear time
# larry
# llaaarrry
# 
# 2: run two loops one to count each charcters count and another to check if the sequence count will match or be greater than the typed
# larry

# ideas:
# -if character pressed was less than the true length of the name then return false immediately
# 
# of the typed string you are examining
# -keep track of the length of each character in the name and use it as basis
# for your condition when the pointer of typed reaches that character
# keep track of its count then if it fails condition then return false
# -keep a pointer for the name
# -keep a pointer for the typed name
# -move pointer such that when it encounters a new character by that time length has already been accumulated for that character
# -when it encounters new character move the other pointer now and accumulate its count
# -once typed count>=name count move the name pointer to count new character length again
# -reset to 0 the count after this 

# to figure out:
# -how to integrate two pointers moving at different speeds in a while loop?
# -assume that there will be an empty character in the typed name that is in the real name
#
#
# -what can be the condition?