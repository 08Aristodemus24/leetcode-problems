class Solution:
    def addStrings(self,num1:str,num2:str)->str:
        result,carry="",0 # initialized to zero 
        i,j=len(num1)-1,len(num2)-1
        
        while i>=0 or j>=0 or carry: # when i and j is 0 and carry is down to its last value loop adds that last value
            if i: # if i and j ptrs are not at zero indeces keep getting values
                carry+=int(num1[i])
            if j: 
                carry+=int(num2[j])
            print(carry)
            result+=str(carry%10) # get the real value of sum val by %base
            
            carry=carry//10 # this will get the carry value and use it for the next digits
            i,j=i-1,j-1


            
            
        # if j not zero
            # get its value
        # add both values
        # if sumval>9 sumval=sumval%10 and carry=sumval//10
        # surprisingly this also works on sumvals<=9 :)
        # and carry as well since it would always be zero if sumvals<=9/base-1

def Main():
    event=Solution()
    #print(event.addStrings("99","189"))
    
Main()
 
# problem:
# ust like adding binary numbers we always need to get the carry value
# and the real sum value of digits

# method:

# ideas:
# we can use an two if statements such that when the other string reaches the end then we should only
# calculate the other longer string to keep adding the carry's if ever there are any
# this is better than using another loop for looping through rest of the digits and then bringing them down for the final
# sum value
# 99349
#   989
# 
# 9+9=18 we % by base which is 10 and get the real value since it is better than subtracting every single time especially when sum vals reach >=20
# getting the carry value is done by using sum val // by number system base
# if pointer i is still pointing to something and j is not keep looping  
# if pointer j is still pointing to something and j is not keep looping
# if pointer i and j is still pointing to something and both run out stop loop
# however there will be the case
# ?what if at the last digit carry + digit is > base-1 then we would have to in this case 9+1 is 10>base-1
# get real val=10%base
# add to value
# then get the carry=10//10 and add to the resultant string
# when j or i reaches 0
# carry is still 1 
#
# CALCULATION:
#  99349
#    989
# 100338

# cases:
# "" + "" since nothing to add pointer i and j points to nothing therefore in the while loop i is 0 and j is 0 and carry is 0

# figure out:

# samples:

