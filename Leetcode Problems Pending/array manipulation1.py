def compare(arr):
    
    i=1
    curmax=arr[0]
    while i<len(arr):
        if curmax<arr[i]:
            curmax=arr[i]
        i+=1

    return curmax

def arrayManipulation(n,queries):
    qlen=len(queries)
    temp=[]

    for i in range(n): 
            temp.append(0)

    if qlen==1:
        lo=queries[0][0]-1
        hi=queries[1][0]-1
        for j in range(lo,hi+1,+1):
            temp[j]+=queries[0][2]

    else:
        for i in range(qlen): # start at zero again
            lo=queries[i][0]-1
            hi=queries[i][1]-1 # get hi and lo indeces of current query
            for j in range(lo,hi+1,+1):
                temp[j]+=queries[i][2] # add

    res=compare(temp)
    return res     

def main():
    que=[
        [2,3,1]
    ]

    optimize_i(que)
    print(que)
    

main()