def searchMatrix(matrix,key,lo,hi):
    col_len=len(matrix[0])
    
    if hi>=lo:
        mid=int((lo+hi)/2)
        row_i=int(mid/col_len)
        col_i=int(mid%col_len)

        if matrix[row_i][col_i]==key:
            return list((row_i,col_i))
        elif key>matrix[row_i][col_i]:
            return searchMatrix(matrix,key,mid+1,hi)
        else:
            return searchMatrix(matrix,key,lo,mid-1)
    else:
        return -1

def main():
    matrix=[
        [1,3,5,7],
    [10,11,16,20],
    [23,30,34,50]
    ]
    
    print(searchMatrix(matrix,3,0,len(matrix)*len(matrix[0])-1))

main()