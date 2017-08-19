#!/bin/bash

python3 ../thread_matrix.py > out_thread.txt

for run in {1..99}
do
  python3 ../thread_matrix.py >> out_thread.txt
done
