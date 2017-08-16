from threading import Thread
import threading
import time
import random

exitFlag = 0

class myThread(threading.Thread):

    def __init__(self, threadID, m1, m2, mf, n, beg, end):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.m1 = m1
        self.m2 = m2
        self.mf = mf
        self.n = n
        self.beg = beg
        self.end = end


    def run(self):
        mult_matrix(self.m1, self.m2, self.mf, self.n, self.beg, self.end)


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
  #with nogil:
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


n = 256

x = create_matrix(n,n)
y = create_matrix(n,n)
z = create_matrix(n,n)

thread1 = myThread(1, x, y, z, n, 0, 128)
thread2 = myThread(2, x, y, z, n, 128, 256)


start = time.time()
thread1.start()
thread2.start()

thread1.join()
thread2.join()

end = time.time()
print(end - start)