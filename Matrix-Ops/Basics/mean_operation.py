class Matrix:
    def __init__(self,data):
        self.data=data
        #Dimensions
        self.rows = len(data)       # Number of rows
        self.columns = len(data[0])     # Number of cols

    #Passing mode if user wants to calculate based on rows and cols
    def mean_calculate(self,mode:str):
        rows = self.rows
        cols = self.columns

        if mode == 'column':
            means = []
            for j in range(cols):
                column_sum = 0
                for i in range(rows):
                    column_sum+=self.data[i][j]
                column_mean = column_sum / rows
                means.append(column_mean)
            return means
        else:
            means = []
            for i in range(rows):
                row_sum = sum(self.data[i])
                row_mean = row_sum/cols
                means.append(row_mean)
            return means


if __name__ == "__main__":
    A = Matrix([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])
    print("Matrix:")
    for row in A.data:
        print(row)

    print(f"\nColumn means: {A.mean_calculate('column')}")
    # Expected: [4.0, 5.0, 6.0]

    print(f"Row means: {A.mean_calculate('row')}")