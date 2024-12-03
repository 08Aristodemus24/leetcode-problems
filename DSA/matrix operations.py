class Matrix:
    def __init__(self):
        pass

    def multiply(self,matrix_x,matrix_y):
        x_rowlen=len(matrix_x)
        x_collen=len(matrix_x[0])

        y_rowlen=len(matrix_y)
        y_collen=len(matrix_y[0])

        # check if matrices can be multplied
        # if not then return
        if x_collen!=y_rowlen:
            return

        # make a new matrix based on number of rows of matrix_x
        # and cols of matrix_y

        for i in range(x_rowlen):
            for j in range(x_collen):
                # ex. of why cols must always be equal to
                # rows

                # matrix_x[0][0]*matrix_y[0][0]
                # matrix_x[0][1]*matrix_y[1][0]
                matrix_x[i][j]*matrix_y[j][i]

    def transpose(self,matrix_x):
        pass

    def inverse(self,matrix_x):
        pass

if __name__ == "__main__":
    matrix=Matrix()
    print("hello")
