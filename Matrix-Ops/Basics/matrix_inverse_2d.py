class Matrix:
    def __init__(self,data):
        self.data=data
        #Dimensions
        self.rows = len(data)       # Number of rows
        self.columns = len(data[0])     # Number of cols

    def inverse_matrix(self):
        if len(self.data) != len(self.data[0] if self.data else 0):
            return "Not 2 X 2 matrix"
        #Calculate values of a,b,c,d
        a,b = self.data[0][0],self.data[0][1]
        c,d= self.data[1][0],self.data[1][1]

        #Calculate Determinant
        determinant =  a*d - b*c
        #check if matrix is invertible or not
        if determinant == 0:
            return "Matrix is singular (determinant = 0), inverse does not exist"

        # Calculate inverse using the formula
        inverse = [
            [d / determinant, -b / determinant],
            [-c / determinant, a / determinant]
            ]
        return Matrix(inverse)

    def print_matrix(self):
        # Matrix Print Method
        lines = []
        for row in self.data:
            row_str = " ".join(str(num) for num in row)
            lines.append(f"[ {row_str} ]")
        return "\n".join(lines)



if __name__ == "__main__":
        A = Matrix([
            [7, 2],
            [17, 5]
        ])

        A_inverse = A.inverse_matrix()
        print(f"INVERSE - {A_inverse.print_matrix()}")