#!/bin/bash

python3 seq_matrix.py > out_seq.txt

for run in {1..99}
do
  python3 seq_matrix.py >> out_seq.txt
done
