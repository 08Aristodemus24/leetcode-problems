def pascalsTri(row):
    
    Tri=[] # store values of triangle
    temp=[] # store row temporarily when created

    if row==0:
        return Tri
    elif row==1: # base case
        return [[1]] # return only list of value one not 2d array
    else:
        Tri.extend(pascalsTri(row-1))
        temp.insert(0,1)
        temp.insert(row-1,1)

        for i in range(1,row-1):
            temp.insert(i,Tri[row-2][i-1]+Tri[row-2][i]) # access the current row and current col elements in the row 

        Tri.append(temp)
        return Tri # once row has been created return its index

def getrow(Tri,row):
    return Tri[row]

def main():
    print(getrow(pascalsTri(1),0)) # entered index must be in array notation


main()
