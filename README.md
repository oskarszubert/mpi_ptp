# Sieve of Eratosthenes with MPI
**Segmented sieve**  - looking for prime numbers in given scope: [m ,n]: m > n > 1.

## Algorithms:
* Sieve of Eratosthenes 
* Valuation of PI uses Euler formula 

## Run program:
To run program run script `run.sh`. \
or `run.sh <number of processors> <begin at> <end at> <granulation>`.\ 

By default program runs Sieve if you want to calculate PI number add one more argv: `2` and start counting from 1.

## MPI
Class Process_farm which contains and support MPI can be used with different algorithms coz its writen universally.
If you want to use Class Process_farm with your own method you need to create:\
	- computation function
	- function for storing and handling result(s)
	- pass type of your result(<list> <int> etc.)


`Python3.6.5`\
`mpi4py` 
