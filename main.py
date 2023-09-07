import copy


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

    def multiply(self, mtx):
        if self.columns == mtx.rows:
            result = Matrix(self.rows, mtx.columns)
            result.matrix = [[sum(self.matrix[i][k] * mtx.matrix[k][j] for k in range(int(mtx.rows)))
                              for j in range(int(mtx.columns))] for i in range(int(self.rows))]
            result.print_matrix()
        else:
            print("Incorrect dimensions of matrices!")

    def multiply_by_number(self, num):
        result = Matrix(self.rows, self.columns)
        result.matrix = [[self.matrix[i][j] * num for j in range(int(result.columns))]
                         for i in range(int(result.rows))]
        return result

    def transpose(self):
        result = Matrix(self.columns, self.rows)
        result.matrix = [[self.matrix[j][i] for j in range(int(self.rows))] for i in range(int(self.columns))]
        result.print_matrix()

    @staticmethod
    def determinant(mtx):
        if len(mtx) == len(mtx[0]):
            if len(mtx) == 1:
                return mtx[0][0]
            elif len(mtx) == 2:
                det = mtx[0][0] * mtx[1][1] - mtx[1][0] * mtx[0][1]
                return det
            else:
                recur = 0
                for i in range(len(mtx)):
                    rex = mtx[0][i] * Matrix.determinant([[el for ind, el in enumerate(matx) if ind != i]
                                                          for matx in mtx[1:]])
                    if i % 2 == 0:
                        recur += rex
                    else:
                        recur -= rex
                return recur
        else:
            print("The matrix must be square!")

    @staticmethod
    def cofactor_matrix(mtx):
        cofa = []
        for i in range(len(mtx)):
            temp_cof = []
            for j in range(len(mtx[0])):
                temp_mtx = copy.deepcopy(mtx)
                temp_mtx.pop(i)
                for matx in temp_mtx:
                    matx.pop(j)
                cof_el = Matrix.determinant(temp_mtx) * (-1)**(i+j)
                temp_cof.append(cof_el)
            cofa.append(temp_cof)
        c = Matrix(len(mtx), len(mtx[0]))
        c.matrix = cofa
        return c

    def inverse(self):
        det = Matrix.determinant(self.matrix)
        if det:
            matrix_c = Matrix.cofactor_matrix(self.matrix)
            matrix_c.multiply_by_number(1 / det).transpose()
        else:
            print("This matrix doesn't have an inverse!")


def menu():
    while True:
        print("\n1) Add matrices\n2) Subtract matrices\n3) Multiply matrices\n4) Multiply matrix by a constant\n"
              "5) Transpose matrix\n6) Calculate a determinant\n7) Inverse matrix\n0) Exit")
        choice = input("You choice: ")
        if choice != "0":
            rows = input("Enter number of rows of matrix: ")
            columns = input("Enter number of columns of matrix: ")
            matrix_a = Matrix(rows, columns)
            print("Enter matrix: ")
            matrix_a.create()

        if choice == "1":
            rows = input("Enter number of rows of second matrix: ")
            columns = input("Enter number of columns of second matrix: ")
            matrix_b = Matrix(rows, columns)
            print("Enter second matrix: ")
            matrix_b.create()

            print("The result is:")
            matrix_a.add(matrix_b)

        elif choice == "2":
            rows = input("Enter number of rows of second matrix: ")
            columns = input("Enter number of columns of second matrix: ")
            matrix_b = Matrix(rows, columns)
            print("Enter second matrix: ")
            matrix_b.create()

            print("The result is:")
            matrix_a.diff(matrix_b)

        elif choice == "3":
            rows = input("Enter number of rows of second matrix: ")
            columns = input("Enter number of columns of second matrix: ")
            matrix_b = Matrix(rows, columns)
            print("Enter second matrix: ")
            matrix_b.create()

            print("The result is:")
            matrix_a.multiply(matrix_b)

        elif choice == "4":
            const = float(input("Enter constant: "))
            print("The result is:")
            matrix_a.multiply_by_number(const).print_matrix()

        elif choice == "5":
            print("The result is:")
            matrix_a.transpose()

        elif choice == "6":
            det = Matrix.determinant(matrix_a.matrix)
            if det is not None and det >= 0:
                print(f"The result is: {det}")

        elif choice == "7":
            print("The result is:")
            matrix_a.inverse()

        else:
            break


menu()
