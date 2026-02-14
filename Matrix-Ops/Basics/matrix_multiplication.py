class MatrixMul:
    def __init__(self,data):
        self.data=data
        #Dimensions
        self.rows = len(data)       # Number of rows
        self.columns = len(data[0])  if self.rows > 0 else 0   # Number of cols

    def print_matrix(self):
        lines = []
        for row in self.data:
            # Convert each number to string and join with spaces
            row_str = " ".join(str(num) for num in row)
            lines.append(f"[ {row_str} ]")
        return "\n".join(lines)

    def get_dimension(self):
        return self.rows, self.columns

    def matrix_multiplication(self,other_matrix):
        if self.columns != other_matrix.rows:
            return "Cannot do matrix multiplication as it has invalid dimensions"

        result_data  = []
        # Loop through each row of first matrix (A)
        for row in range(self.rows):
            new_row = []
            # Loop through each column of second matrix (B)
            for col in range(other_matrix.columns):
                dot_product = 0
                for k in range(self.columns):
                    # A[i][k] * B[k][j]
                        dot_product += self.data[row][k]*other_matrix.data[k][col]
                new_row.append(dot_product)
            result_data.append(new_row)
        return MatrixMul(result_data)

    #Fast and easy
    def matrix_multiplication_using_Transpose(self,other_matrix):
        if self.columns != other_matrix.rows:
            return "Cannot do matrix multiplication as it has invalid dimensions"

        # Step 1: Transpose B
        other_t = list(zip(*other_matrix.data))
        result_data = []
        # Step 2: For each row in A
        for row_a in self.data:
            new_row = []
            # Step 3: For each column in B (now rows in other_T)
            for col_b in other_t:
                # Step 4: Calculate dot product
                dot_product = 0
                for a, b in zip(row_a, col_b):
                    dot_product += a * b
                new_row.append(dot_product)
            result_data.append(new_row)
        return MatrixMul(result_data)


if __name__ == "__main__":
    # Test 1: Valid multiplication (2×3) × (3×2) = (2×2)
    A = MatrixMul([
        [1, 2, 3],
        [4, 5, 6]
    ])

    B = MatrixMul([
        [7, 8],
        [9, 10],
        [11, 12]
    ])

    print("Matrix A (2×3):")
    print(A.print_matrix())
    print(f"\nMatrix B (3×2):")
    print(B.print_matrix())

    print(f"\nA × B = (2×2):")
    C = A.matrix_multiplication(B)
    print(C.print_matrix())

