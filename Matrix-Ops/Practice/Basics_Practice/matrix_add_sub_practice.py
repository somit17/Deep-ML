class MatrixAddSub:
    def __init__(self,data):
        self.data=data
        #Dimensions
        self.rows = len(data)       # Number of rows
        self.columns = len(data[0])  if self.rows > 0 else 0   # Number of cols

    def shape(self):
        # Return dimensions
        return self.rows,self.columns

    def print_matrix(self):
        lines = []
        for row in self.data:
            # Convert each number to string and join with spaces
            row_str = " ".join(str(num) for num in row)
            lines.append(f"[ {row_str} ]")
        return "\n".join(lines)

    def get_dimension(self):
        return self.rows,self.columns


    def matrix_addition(self,other_matrix):
        if self.get_dimension() != other_matrix.get_dimension():
            return "Cannot add matrices bcoz dimensions does not match"

        result_data = []
        for i in range(self.rows):
            new_row = []
            for j in range(self.columns):
                # Add elements
                sum_val  = self.data[i][j]+other_matrix.data[i][j]
                new_row.append(sum_val)
            result_data.append(new_row)
        return MatrixAddSub(result_data)

    def matrix_subtraction(self,other_matrix):
        if self.get_dimension()!=other_matrix.get_dimension():
            return "Matrix substraction cannot be done bcoz of invalid dimensions"

        result_data = []

        for row in range(self.rows):
            new_row = []
            for col in range(self.columns):
                sub_val = self.data[row][col] - other_matrix.data[row][col]
                new_row.append(sub_val)
            result_data.append(new_row)
        return MatrixAddSub(result_data)



if __name__ == "__main__":
    # Create matrix
    # Create two 3×3 matrices
    A = MatrixAddSub([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    B = MatrixAddSub([
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ])

    print("Matrix A:")
    print(A.print_matrix())
    print(f"\nMatrix B:")
    print(B.print_matrix())

    print(f"\nAddition of Matrix A and B (saving in C):")
    C = A.matrix_addition(B)

    print(C.print_matrix())

    print(f"\nSubtraction  of Matrix A and B (saving in D):")
    D = A.matrix_subtraction(B)
    print(D.print_matrix())