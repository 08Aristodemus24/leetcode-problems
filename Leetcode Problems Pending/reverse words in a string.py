class Solution:
    def reverseWords(self,sen:str)->str:
        arr=sen.split(' ')
        i=0

        print(arr)
        while i<len(arr):
            if arr[i]=='':
                arr.remove(arr[i])
            else:
                i+=1
        return ' '.join(arr)


# problem:
# given a sentence string
# reverse all the words in that sentence
# "hello world!"
# "world! hello"
# "larry miguel cueva"
# "cueva miguel larry"
# note that whitespaces ahead of the any starting string should not be present

# method:
# remove all white spaces first

# idea:
# 1. like reversing a strings characters we get the lo and hi indeces of each string in the sentence
# - but since the string is a sentence with multiple strings there is no way to reverse strings
# in string form since each character is operated by indeces
# what we first have to do is convert the sentence into a list of strings such that each string only
# operates by one index and from there can be reversed using the reverse function
# then converted back to a string
# - but first since there is no telling if there is a tailing or a leading whitespace
# - there is no telling whether there are white spaces in between
# bottom line remove all unecessary white spaces
# "  hello  world "
#  we use the split function 
# we loop through

# figure out:

# cases:

# samples:

def Main():
    string=" my name  is"
    event=Solution()
    print(event.reverseWords(string))

Main()
