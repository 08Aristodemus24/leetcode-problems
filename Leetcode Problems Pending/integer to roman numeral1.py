

class RomanNumeral:
    def intToRoman(self,num:int)->str:
        keys={1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
        length=len(str(num))
        string=''
        
        arr=[int(x) for x in str(num)]
        
        i=0
        while i<length: # this will convert each digit of the array to roman numerals
            string=string+keys[pow(10,length-(i+1))*arr[i]] # equation to convert to roman numeral
            i+=1
        
        return string



def Main():
    num=RomanNumeral()
    result=num.intToRoman(1495)
    print(result)
    


Main()

# pattern is that everytime roman numeral is about to be changed
# like from a number to a 5,10,50,100
# previous roman numeral is I as it approaches 5 
# element nearing it is 4 is changed to I to IV and then V
# VI to IX to X
# XI to XIV to XV
# XVI to XIX to XX

# for each place we can use the different values from the roman numerals
# if for that place it is less than the next numeral then concatenate in reverse ex. 900 since 900<1000 CM
# ex. 800 since 800 < 1000 since 8 is VII and its number of zeroes is a hundred C

# ex. 1945
# first place 1000 is converted to M
# second place is 900 check if precedence is lesser than next numeral which is 1000 concatenate C then D
# third place 40 is check if precedence is lesser than next numeral which is 50 concatenate X then L

# method 1: convert to string
# since it is an integer
# convert to string and assign to a variable
# loop through each number
# 1945 1 is in 4th place
# however there is no indicator that it is in 4th place this is why we need to somehow do an operation that extracts each digit
# 1945 t

# method 2: extract each digit by using number to get length by converting to string
# list all keys first especially cases where roman numerals have lesser precedence
# get length by converting number to string
# run while loop that extracts the place of the current number
# ex. 1945 1000 is calculated by 10^length-1 x current digit such that it starts from first index to last index
#
# but how do we convert 3 to III or 8 to VIII