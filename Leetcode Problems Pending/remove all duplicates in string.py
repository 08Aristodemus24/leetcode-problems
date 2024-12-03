class Solution:
    def removeDuplicates(self,string:str)->str:
        
        # create an empty stack
        # initial value of top element
        stack=['#']
        
        # if there is no duplicate found then flag will be
        # set to false
        flag=True

        i=0
        while :
            while True:
                if string[i]==stack[len(stack)-1]
                    flag=True
                    i+=1
                elif string[i]!=stack[len(stack)] && flag==True:
                    stack.pop()
                    stack.append(string[i])
            


# problem:
# given a string "abbaca"
# remove all duplicates and all possible duplicates when
# duplicates are removed

# idea:
# - remove all duplicates first
# - when duplicates are removed then remove
# possible duplicates
# - do this process until all duplicates are gone
# 
# - declare empty stack called stack
# - 

# method:

# cases/samples:
# 1. abbaca
#
# 2. cabbbbacca
# - push c 

# figure out:
