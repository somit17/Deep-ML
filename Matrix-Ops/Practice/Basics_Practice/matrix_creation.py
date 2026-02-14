class Matrix:
    def __init__(self, rows,cols,fill_value=0): #By Default value is  0
        self.matrix = []
        self.rows = rows
        self.cols = cols
        for i in range(rows):
            # Each row has 'cols' copies of fill_value
            row = [fill_value] * cols
            self.matrix.append(row)

    def print_matrix(self):
        #Matrix Print Method
        lines = []
        for row in self.matrix:
            row_str = " ".join(str(num) for num in row)
            lines.append(f"[ {row_str} ]")
        return "\n".join(lines)

if __name__ == "__main__":
    A = Matrix(3,3)
    print(f"Matrix  A (By Default Values 0)=  {A.print_matrix()}")

    B = Matrix(1,3,1)
    print(f"Matrix B (By Default Values 1)=  {B.print_matrix()}")