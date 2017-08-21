# parallel-python

Final assignment for the Introduction to Parallel Programming class at Federal University of Pelotas.

This work is an exploratory research about parallel programming in Python. To evaluate the viability we did three implementations of matrix multiplication:

- sequential;
- parallel, using native threads from Python and;
- parallel, using the API mpi4py.

The matrices used for the calculation were of the 256x256 size. We run 100 times each algorithm, where we have used statistics methods for the speed-up evaluation. The results presented the MPI implementation as the one with the better performance.



### Requirements

- Python 3.x+
- Cython
- A functional MPI 1.x/2.x/3.x implementation like MPICH or Open MPI built with shared/dynamic libraries.

### Running

Sequencial

`
  $ python3 seq_matrix.py
`

Threads

`
  $ python3 thread_matrix.py
`

MPI

`
  $ mpirun -np 2 python3 mpi_matrix.py
`

### References

Cai, X., Langtangen, H. P., and Moe, H. (2005). **On the performance of the python
programming language for serial and parallel scientific computations**. *Scientific Pro-
gramming*, 13(1):31–56.

Dalcin, L. (2017). **mpi4py**. Available at: [https://bitbucket.org/mpi4py/mpi4py.git](https://bitbucket.org/mpi4py/mpi4py.git)

Dalcı́n, L., Paz, R., and Storti, M. (2005). **Mpi for python**. *Journal of Parallel and
Distributed Computing*, 65(9):1108–1115.

Github (2017). A small place to discover languages in github. Available at: [http://githut.info/](http://githut.info/)

Miller, P. (2002a). pympi: **An introduction to parallel python using mpi**. Livermore
National Laboratories, 11.

Miller, P. J. (2002b). **Parallel, distributed scripting with python**.

Python.org (2017). **Global interpreter lock**. Available at: [https://wiki.python.org/moin/GlobalInterpreterLock](https://wiki.python.org/moin/GlobalInterpreterLock)

Scott, L. R., Clark, T., and Bagheri, B. (2005). *Scientific Parallel Computing. Princeton
University Press*, Princeton, NJ, USA.

Singh, N., Browne, L.-M., and Butler, R. (2013). Parallel astronomical data processing
with python: Recipes for multicore machines. *Astronomy and Computing*, 2:1–10.
