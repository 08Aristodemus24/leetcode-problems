def reverse(nums,lo,hi):
    if lo>=hi:
        return
    temp=nums[lo]
    nums[lo]=nums[hi]
    nums[hi]=temp
    reverse(nums,lo+1,hi-1)

def numrot(nrot,length):
    num=0
    while num<=nrot:
        num+=length

    num=num-length
    nrot=nrot-num
    return nrot

def rightRotate(nums,k):
    length=len(nums)
    k=numrot(k,length) # optimize number of rotations first
    if length==0 or length==1 or k==length:
        return

    reverse(nums,k)
    reverse(nums,0,k-1)
    reverse(nums,k,length-1) 

