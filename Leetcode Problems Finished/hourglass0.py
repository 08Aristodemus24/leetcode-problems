import math

def compare(arr):
    i=1
    curmax=arr[0]
    while i<len(arr):
        if curmax<arr[i]:
            curmax=arr[i]
        i+=1

    return curmax

def hourglassSum(glass):
    temp=[] # initialize max to 0
    for row in range(4):
        for col in range(4):
            res=glass[row][col]+glass[row][col+1]+glass[row][col+2]+glass[row+1][col+1]+glass[row+2][col]+glass[row+2][col+1]+glass[row+2][col+2]
            temp.append(res)

    return compare(temp)

def main():
    arr=[
        [1 ,1,1,0,0,0],
[0, 1 ,0 ,0 ,0 ,0],
[1 ,1 ,1 ,0 ,0 ,0],
[0 ,0 ,2 ,4 ,4 ,0],
[0, 0 ,0 ,2 ,0 ,0],
[0 ,0 ,1 ,2 ,4 ,0]
    ]
    print(hourglass(arr))


main()