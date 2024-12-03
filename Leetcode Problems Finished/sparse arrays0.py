def sparse(strings,queries):

    temp=[]
    count=0
    
    for i in range(len(queries)):
        for string in strings:
            if queries[i]==string:
                count+=1

        temp.insert(i,count)
        count=0 # reset count

    print(temp)

def main():
    strings=["aba","ab","aba","xzxb"]
    queries=["aba","xzxb","ab"]
    sparse(strings,queries)

main()
    