from math import gcd as gcf

def matrixReshape(matrix,new_row,new_col):
    row_len=len(matrix)
    col_len=len(matrix[0])
    matrix_len=row_len*col_len

    if matrix_len==1 or matrix_len==0 or matrix_len!=new_row*new_col: # [[]],[[1]],[[],[]] 
        return matrix
    else:
        temp=[]
        for i in range(row_len):
            for j in range(col_len):
                temp.append(matrix[i][j])
        matrix=[]
        for i in range(new_row): # clear old matrix and set up new matrix0
            matrix.append([])

        for i in range(len(temp)): # map temp arrays elements to the new matrix
            row_len=int(i/new_col)
            col_len=int(i%new_col)
            matrix[row_len].insert(col_len,temp[i])

        return matrix
def main():
    nums=[
        [1,2],
        [3,4]
        ]
    nums=matrixReshape(nums,1,4)
    for num in nums:
        print(num)

main()


