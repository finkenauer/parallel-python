import random
import time

def create_matrix(n_rows, n_columns):
    matrix = []
    line = []
    element = 0

    while len(matrix) != n_rows:
        n = random.randint(1,99)
        line.append(n)
        element = element + 1


        if len(line) == n_columns:
            matrix.append(line)
            line = []

    return matrix


# M1 = matrix 1, M2 = matrix 2, MF = final matrix
# n = size of matrices, beg = beginning of iteration, end = end of iteration
def mult_matrix(m1, m2, mf, n, beg, end):

    # row
    for i in range(beg, end):
        # line
        for k in range(n):
            elem = 0
            # column
            for j in range(n):

                elem = elem + (m1[i][j] * m2[j][k])
                mf[i][k] = elem

            # print(elem)


n = 1024

x = create_matrix(n,n)
y = create_matrix(n,n)
z = create_matrix(n,n)

start = time.time()
mult_matrix(x, y, z, n, 0, n)
end = time.time()

# mult_matrix(x, y, z, n, 2, 4)
# print(z)
print(end - start)
