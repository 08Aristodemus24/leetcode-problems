from math import gcd

# this left rotation will run at less than O(n2) time
# using juggling algorithm

def numrot(nrot,length):
    num=0
    while num<=nrot:
        num+=length

    num=num-length
    nrot=nrot-num
    return nrot

def leftrotate(len):
    gcd=gcd(len(arr),nrot)
    # rotation cases
    # if n rotation is 0 or is equal to length return
    # if n rotation is greater than length optimize rotation number
    
    # lenth cases
    # if length is 0 or 1 return
    # if length is greater than or equal to 2 rotate

    # juggling algorithm length cases
    # if length is 2 




def main():
    arr=[1,2,3,4,5]

    print(eucl(7,3))

main()