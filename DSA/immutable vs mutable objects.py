def main():
    # immutable
    a=10 
    b=a
    b=90
    print(a)
    print(b)

    # mutable
    x=[1,2,3,4,5]
    y=x
    y[0]=2
    print(x)
    print(y)

    # mutable but when assigned to others trait of object is changed
    v=[1,2,3,4,5]
    w=v
    w=[2,4,6,8,0]
    print(v)
    print(w)

    # immutable
    stringx="hello"
    stringy=stringx
    stringy=stringy.replace("h","a")
    print(stringx)
    print(stringy)

    # immutable
    ptr1=None
    ptr2=ptr1
    ptr2=10
    print(ptr1)
    print(ptr2)

    # mutable
    ptrlist1=[1,None]
    ptrlist2=ptrlist1
    ptrlist2[1]=10
    print(ptrlist1)
    print(ptrlist2)

    # mutable
    dict1={"name":"larry","age":0}
    dict2=dict1
    dict2["age"]=9
    print(dict1)
    print(dict2)

    set1={1,2,3,4,5}
    set2=set1
    
    print(set1[0])
    print(set2)
main()