# given sorted arrays nums1 and nums2
# place nums2 to nums1 such that nums1 will still be sorted after insertion of
# elements of nums2
# note that extra space of nums1 is <= to length of nums2
# 1,2,3,0,0,0 extra space 3, to be added is 4,5,6

# length cases
# nums1 is 0 then just insert nums2
# -using extend
# nums2 is 0 then just return
# nums1 and nums2 is 0 then return
# since length of both is already given use m and n

# method 1: 
# nums1 and nums2 have 1 or more elements
# [1,0] and [2]
# declare two pointers to traverse in O(n) time
# check each element whether that element is greater or lesser than the other pointer
# [1,0], [2] inserted in [index 1]
# [1,2,2,3,4,5,0,0,0] and [2,3,4]
# find the element that is lesser than pointer 2's value
# 1 < ptr[0] insert at [index of 1+1]
# until no new lesser value is found keep traversing through nums1
# when value is inserted move ptr2 to next element until length
# loop depends on the number of elements in nums2, when all values are inserted stop loop

# method 2: remove zeroes first
# 
def merge(nums1,m,nums2,n):
    if m==0:
        nums1[m:]=nums2
        return
    elif n==0:
        return
    elif m==0 and n==0:
        return
    else:
        nums1[m:]=nums2
        nums1.sort()

def main():
    nums1=[1,0,0]
    nums2=[4,5,6]
    merge(nums1,1,nums2,3)
    print(nums1)

main()



