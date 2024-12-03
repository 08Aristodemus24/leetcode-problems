def setZeroes(matrix):
    # given a matrix m * n set all the rows and columns of 0 detected to zero also
    # [1,1,0]
    # [1,1,1]
    # [1,1,1]
    # set row of 0 which is in row 0 and column 2 to zero
    # how do we check if an element is a true zero by definition a true zero is the zero that has been scanned before the change began
    # it is also a zero with both zeroes of its columns and rows and if its zero and either rowcol!=zero and rowcol==zero then it is not a true zero

    # length case 1: matrix is 1x1[[1]],1x0[[]] or 0x0[] return
    # length case 2: matrix is 1x2[[1,0]] calculate!

    # method 1
    # do linear scan by mapping each element to a simple array element until range m*n
    # row/collen and col%collen
    # if zero is detected get its row and set entire row to zero
    # get its column and set entire column to zero

    # what if zero is detected but it is part of the column and row set to zero
    # [0,1,0]
    # [1,1,1]
    # [1,1,1]
    # either that zero has no column/row or has a row of zeroes from the previous modification
    # however zeroes may be at corner, edges, 
    # if equal to zero, and rowcol+1!=zero or ro
    
    # method 2
    # once zero is encountered save in temp var
    # when next zero is found
    # DEADEND since all zeroes would still be affected

    # method 3 (m+n) or (m*n) space
    # get all positions first of zeroes first and 
    # determine if its a corner, edge, or element in
    # what is common in corner,edge, and element in
    # corners and edges all are outside the in elements
    # zeroes can be filled by using their row number
    # and column-1 until 0 
    # to set every zero determine its row iterate from 0 to length of that row [row][0<number of col]
    # for setting of the columns go from 0 to number of rows using that column [0<number of rows][col]

def main():
    matrix=[
        [1,1,0], # row 0 col 2
        [0,1,1], # row 1 col 0
        [1,1,1]
        ]

main()