class IdentityMatrix:
    def __init__(self,n):

        self.idt_matrix = []
        for i in range(n):
            row = [0] * n
            # Put 1 on the diagonal (where row index == column index)
            row[i] = 1
            self.idt_matrix.append(row)

    def __str__(self):
        """Pretty print the matrix"""
        lines = []
        for row in self.idt_matrix:
            row_str = " ".join(str(num) for num in row)
            lines.append(f"[ {row_str} ]")
        return "\n".join(lines)

if __name__=="__main__":
    #Create identity Matrix
    A = IdentityMatrix(3)
    print(f"A Matrix : {A}")

    B = IdentityMatrix(1)
    print(f"B Matrix : {B}")