class Matrix:
    def __init__(self,data):
        self.data=data
        #Dimensions
        self.rows = len(data)       # Number of rows
        self.columns = len(data[0])     # Number of rows

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


if __name__ == "__main__":
    # Create matrix
    A = Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    print(f"Shape i.e Rows and Cols = {A.shape()}\n")
    print(f"Raw data : {A.print_matrix()}")
