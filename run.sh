#!/bin/bash

if [[ $# -eq 4 ]] ; then
	mpiexec -n $1 -host localhost python3 src/main.py $2 $3 $4

elif [[ $# -eq 3 ]] ; then
	mpiexec -n $1 -host localhost python3 src/main.py $2 $3
else 
	printf '[ 1 ] Segmented Sieve,\n[ 2 ] PI number.\n' 
	read -p 'Choice: ' trigger 
fi

if [[ $trigger == 1 ]]; then
	read -p 'How many processors: ' proc
	read -p 'Begin at: ' begin_at
	read -p 'End at: ' end_at
	read -p 'Granulation: ' granulation

	mpiexec -n $proc -host localhost python3 src/main.py $begin_at $end_at $granulation
elif [[ $trigger == 2 ]]; then
	read -p 'How many processors: ' proc
	read -p 'Scope: ' scope
	read -p 'Granulation: ' granulation

	mpiexec -n $proc -host localhost python3 src/main.py $scope $granulation

else
	echo 'Try again!'
fi