def removeelement(arr,val):
    # return the length of array
    # remove all elements with value of val using pop at certain index
    # after removing one element update length
    
    # length cases
    # 1. 0 el, 1 el return arr
    
    # 2. 2 elements
    # duplicate element cases for length 2
    # a. duplicate is present
    # pop element by checking if arr[i]==val
    # index position will have new number since previous element popped
    # update length
    # b. return arr

    # 3. 3 elements
    # duplicate element cases for length 3
    # a. duplicate is present
    # pop element by checking again=
    # inner loop will keep deleting all adjacent elements with val value
    i=0
    length=len(nums)
    while i<length:
        while True:
            if nums[i]==val and i==length-1: # position will not exist if 
                arr.pop(i)
                length=len(arr) # update length of array
                break
            elif arr[i]==val: # check if pointer i is at last node
                arr.pop(i)
                length=len(arr)
            else:
                break
        i+=1
    return length

    
