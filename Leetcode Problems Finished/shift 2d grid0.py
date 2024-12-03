def numrot(nrot,length):
    num=0
    while num<=nrot:
        num+=length

    num=num-length
    nrot=nrot-num
    return nrot

def rotateMatrix(matrix,k):
    # to access each element in array form map array index to row and col index
    rlen=len(matrix)
    clen=len(matrix[0])
    matrixlen=clen*rlen
        
    # optimize rotation number using function below
    k=numrot(k,matrixlen)
        
    if len(matrix)==0:
        return matrix

    elif len(matrix)==1 and len(matrix[0])==1:
        return matrix
    
    elif k==matrixlen:
        return matrix

    else:
        reverseMatrix(matrix,0,matrixlen-1) # rotate matrix first
        reverseMatrix(matrix,0,k-1) # rotate out of bound elements 0 to 3 exclusively
        reverseMatrix(matrix,k,matrixlen-1) # rotate all elements still in matrix
        return matrix

def reverseMatrix(matrix,lo,hi): # matrix len must be calculated in order to work
    #rlen=len(matrix)
    clen=len(matrix[0])
    lo_row=int(lo/clen)
    lo_col=int(lo%clen)
    hi_row=int(hi/clen)
    hi_col=int(hi%clen)
    if lo>=hi:
        return
    # swap matrix elements
    temp=matrix[lo_row][lo_col]
    matrix[lo_row][lo_col]=matrix[hi_row][hi_col]
    matrix[hi_row][hi_col]=temp
    reverseMatrix(matrix,lo+1,hi-1)

def main():
    matrix=[[1,2,3],[4,5,6],[7,8,9]]
    rotateMatrix(matrix,12)
    print(matrix)
    
main()

