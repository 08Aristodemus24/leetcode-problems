class Solution:
    def octalToASCIICipher(self,s:str)->str:
        keys={"1":"a","2":"b","3":"c","4":"d","5":"e","6":"f","7":"g","8":"h","9":"i",
        "10":"j","11":"k","12":"l","13":"m","14":"n","15":"o","16":"p","17":"q","18":"r",
        "19":"s","20":"t","21":"u","22":"v","23":"w","24":"x","25":"y","26":"z"} # data set to base on

        code=""
        i,hi=0,len(s)-1
        while i<hi+1 and i<hi-1: # when i reaches 2nd to the last element end loop since i will be out of range if i+2
            if s[i+2]=='#':
                code+=keys[s[i:i+2]] # slice the string and get the i value until the hash
                i+=3
            else:
                code+=keys[s[i]] # get current i's value in dictionary 
                i+=1
        while i<hi+1: # will be executed for remaining char/last 2 chars, loop stopped because i+2 will out of range for these i's
            code+=keys[s[i]]
            i+=1
        return code

    def asciiToOctalCipher(self,s:str)->str:
        pass

def Main():
    enc="1223#421#1"
    enc2="1214232342342323#123#122#"
    event=Solution()
    print(event.octalToASCIICipher(enc2))
Main()

# cases:

# figure out:
# traversal for characters with hashes
# starting at beginning advancing ahead will result in out of range cases but how to fix
# starting at end and appending all the characters 