#!/bin/bash

mpirun -np 2 ../python3 mpi_matrix.py > out_mpi.txt

for run in {1..99}
do
  mpirun -np 2 ../python3 mpi_matrix.py >> out_mpi.txt
done
