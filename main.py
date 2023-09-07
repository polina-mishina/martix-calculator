class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[]]

    def create(self):
        self.matrix = [[float(n) for n in input().split()] for _ in range(int(self.rows))]

    def print_matrix(self):
        for i in range(int(self.rows)):
            for j in range(int(self.columns)):
                print(self.matrix[i][j], end=' ')
            print()

    def add(self, mtx):
        if self.rows == mtx.rows and self.columns == mtx.columns:
            result = Matrix(self.rows, self.columns)
            result.matrix = [[self.matrix[i][j] + mtx.matrix[i][j] for j in range(int(result.columns))]
                             for i in range(int(result.rows))]
            result.print_matrix()
        else:
            print('The dimensions of the matrices do not match!')

    def diff(self, mtx):
        if self.rows == mtx.rows and self.columns == mtx.columns:
            result = Matrix(self.rows, self.columns)
            result.matrix = [[self.matrix[i][j] - mtx.matrix[i][j] for j in range(int(result.columns))]
                             for i in range(int(result.rows))]
            result.print_matrix()
        else:
            print('The dimensions of the matrices do not match!')
