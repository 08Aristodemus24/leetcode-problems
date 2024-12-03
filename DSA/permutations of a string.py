class Solution:
    def strPermute(self,word:str)->list:
        return self._strPermute(list(word),0,len(word)-1)
        
    def _strPermute(self,word:list,lo:int,hi:int)->str:
        if lo==hi:
            return [word]

        result=[]
        temp=word
        for i in range(lo,len(temp)):
            # swap the current lo with all the chars
            # in the string 
            # e.g A is current lo so swap with
            # A,B,C,D
            temp[lo],temp[i]=temp[i],temp[lo]

            # reduce sample space of swapping
            # by increasing lo index so that
            # next time B is lo and A will not be swapped 
            # any more
            # convert to string again
            result=result+(self._strPermute(temp,lo+1,hi))

            # after saving the newly modified list revert
            # list back to original to avoid copoies since 
            # lists are mutable then start modification again
            temp[lo],temp[i]=temp[i],temp[lo]

        return result

            


# problem:
# given a string return all its permutations such
# that all permutations are stored in a list


# method:

# idea:
# - e.g. for a string ABCD
# - we switch out the first index always with the including with itself and the next coming indeces 
# - ABCD
# - swap with the first index
# - pass the string again but with restriction that the 1st index would not be touched anymore
# - and that we should only swap the 2nd index which is b with itself and the next coming indeces 
# - we fix the position of a such that when swappped we dont modify it anymore1 

# cases/samples:
# 1. single string 'A'
# we swap the index 0 at it first index 
# when then 

# figure out:
# 1. what can be the base case?

# 2. how do we fix the position of a swapped letter? like  the bubble 
# sort algorithm we reduce the sample space of the string by increasing 
# the lo and hi indeces that we should be working on

# 3. since a string is immutable how do we swap?
#  
# 4. especially when we do this in the case of lists where it is mutable, 
# how do we swap without changing its elements position?


# diagram:

if __name__ == "__main__":
    event=Solution()
    print(event._strPermute([1,2,3],0,3))
