# pre-equisite: hash maps/hash tables

def contNearDuplicate(arr,k):
    # just like any duplicate number it always has 2 different indeces but those indeces contain the
    # same values of each other
    # [1,2,3,1]
    # abs difference between i=0 and i=3 is 3 
    # given the target which is 3 calculate the abs diff each time a duplicate is found
    # sorting cannot work since indeces would change
    
    # length cases
    # 1 or 0 return false
    # 2 check using if, if yes then return true

    # method 1: brute force
    # if found dup num[i] and num[j]
    # check if abs i and j <= target
    # absolute difference between i and j is at most k or can be less than k
    
    # method 2:
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                continue
            elif arr[i]==arr[j] and abs(i-j)<=k:
                return True
    return False

def main():
    arr=[99,99]
    print(contNearDuplicate(arr,2))

main()