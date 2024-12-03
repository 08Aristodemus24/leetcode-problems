class Solution:
    def infixToPostfix(self,exp:str)->str:
        
        keys={
            '*':2,
            '/':2,
            '+':1,
            '-':1,
            '(':4,
            ')':4,
            '^':3
        }

        stack=[]
        res=''
        for val in exp:
            if val.isalnum():
                res = res + val
            
            # if stack is empty just append
            # also if stack is not empty
            # compare to top element current non alpha num char
            elif stack and keys[val] <= keys[stack[-1]]:
                res = res + stack.pop()
                stack.append(val)
            
            elif stack and val == ')'
                pass
            # if stack is empty this will
            # execute
            else:
                stack.append(val)

        return res

# problem:
# the human way to convert this x^y/(5*z)+2 to this xy^5z*/2+
# is to identify the precedence of each operator
# +,-,*,/,^,( or )
# () has the highest precedence
# ^ has the 2nd highest precedence
# * and / has the 3rd highest precedence
# + and - has the 4th highest precedence

# method:

# idea:
# - the only operators we need to worry about is the 4 basic operations 
# and also the exponent operator
# - we check if the string has a parentheses
# if there is then we evaluate that expression first
# if alphanum push add to string
# if encountered operand and stack is empty
# then push it
# if encountered operand and stack is not empty then
# still push it
# 

# else move on
# - have an empty stack ready
# -

# cases/samples:
 
# figure out:

if __name__ == "__main__":
    event=Solution()
    print(event.infixToPostfix("x^y/(5*z)+2"))