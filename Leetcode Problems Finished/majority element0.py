def majElement(nums):
    # given n number of elements determine the elements with highest occurence
    # majority element is the element which appears more than n/2 times
    # majorty element in array of size 1 must be more than 0.5 or 0
    # majority element in array of size 2 must be more than 1 and the same as previous appearance
    # 
    # method 1: brute force n^2
    # method 2: sort elements first so that occuring elements are adjacent
    # 
    # given [1,2,2,4,5,5,2,1,1,1]
    # when sorted all majority elements seem to be adjacent to each other
    # start at 0 until length -1
    # use temp variable to store first trait of majority element
    # when equal to elements in the array add one to the count
    # then when scan has reached a new element set temp to that new numbers trait
    # and start count again
    # keep track of old count and set to current max if that max is broken by the temps new count set temp to that current max
    # [1,1,1,1,2,2,2,4,5,5]
    # temp is set to 1
    # tempcount is 0 for current temp
    # set max count to 0 initially when temp has found another number set max count to the tempcount
    # reset temp count to 0 and begin scan again
    # everytime there is occ +1 to count

    nums.sort() # []
    t_count=0
    max_count=0
    temp_el=nums[0]
    max_el=nums[0] # may change when max_count is broken
    for i in range(len(nums)):
        if temp_el!=nums[i]: # 2 is approached
            if max_count<t_count:
                max_el=temp_el
                max_count=t_count
            temp_el=nums[i] 
            t_count=0
        t_count+=1    

    if max_count<t_count:
        max_el=temp_el

    return max_el

def main():
    nums=[1,2,2,2,2,3,3,3,3,3,3,1,1,1,1] # assume that array will not have empty elements and maj element always exists
    maj=majElement(nums)
    print(maj)

main()