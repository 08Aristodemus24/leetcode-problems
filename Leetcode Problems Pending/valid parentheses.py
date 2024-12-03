class Solution:
    def validParentheses(self, parses: str) -> bool:
        keys={
            "(":")",
            "{":"}",
            "[":"]"
        }
        
        stack=[]
        for char in parses:
            # if val is either these openings find its closing
            if char=='(' or char=='[' or char=='{':
                stack.append(char)
            # if val has encountered a new char
            elif not len(stack):
                return False
            elif char==keys[stack[len(stack)-1]]:
                stack.pop()
            else:
                return False
                
        return False if len(stack)!=0 else True

def Main():
    event=Solution()
    print(event.validParentheses("[](([]))[[]]"))

Main()





            
# problem:
# characters () {} []
# return a boolean value true only if
# string entered has valid parentheses entered 
# valid parentheses include:
# brackets that have been detected and have an end
# ex. ()[] length is 4 parentheses is detected first therefore it has to find its
# match because if it doesnt then string entered is invalid
# ([)]
# parentheses is detected therefore it must find its matching parentheses
# however bracket is found so it must change its current char to check if
# bracket has a match if it does
# revert back to the old parentheses and check if next coming characters are parentheses
# or not
# if not then we have to check again if that char has a match

# method:
# -we initialize the stack to the first element in the string
# -we set the ptr to the last element always
# -loop from 1 to < length
# -we compare the ptr to the element
# -if it is a diff element there are two scenarios ( to }]) or {[(
#   if element is a diff go to dict and check if that is a closing
#   if element is a diff go to dict and check if it is another but not closing
# -if it is the same element we need to append it to the stack
#   set the pointer to that element and find its pair
#   the priority is to find its pair
# -if it is a 

# idea:
# -whenever we find a different opening bracket we push it to the stack
# -then we find its closing bracket
# if it is a closing bracket we revert back to the previous bracket
# and find its respective closing bracket
# we could use maintain a previous and current pointers
# previous will be the one to maintain the old char that has been replaced by the new char
# which is the current which holds the current char

# figure out:
# how would we know if its a closing bracket

# cases:
# brackets:
# ptr current finds a char then find its matching closing

# sample:
# {([()]()}
# ^
