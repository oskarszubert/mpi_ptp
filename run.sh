#!/bin/bash

if [[ $# -eq 4 ]] ; then
	
	if [[ $4 -lt $1 ]]; then
		printf 'Cannot pass granulation less than number of proc!\n'
		printf 'Set: granulation = number of proc.\n------------\n'
		mpiexec -n $1 -host localhost python3 src/main.py $2 $3 $1
	else
		mpiexec -n $1 -host localhost python3 src/main.py $2 $3 $4
	fi

elif [[ $# -eq 3 ]] ; then

	if [[ $3 -lt $1 ]]; then
		printf 'Cannot pass granulation less than number of proc!\n'
		printf 'Set: granulation = number of proc.\n------------\n'

		mpiexec -n $1 -host localhost python3 src/main.py $2 $1
	else
		mpiexec -n $1 -host localhost python3 src/main.py $2 $3
	fi

else 
	printf '[ 1 ] Segmented Sieve,\n[ 2 ] PI number.\n' 
	read -p 'Choice: ' trigger

	if [[ $trigger == 1 ]]; then
		read -p 'How many processors: ' proc
		read -p 'Begin at: ' begin_at
		read -p 'End at: ' end_at
		read -p 'Granulation: ' granulation

		if [[ $granulation -lt $proc ]]; then
			printf 'Cannot pass granulation less than number of proc!\n'
			printf 'Set: granulation = number of proc.\n------------\n'
			mpiexec -n $proc -host localhost python3 src/main.py $begin_at $end_at $proc
		else
			mpiexec -n $proc -host localhost python3 src/main.py $begin_at $end_at $granulation
		fi

	elif [[ $trigger == 2 ]]; then
		read -p 'How many processors: ' proc
		read -p 'Scope: ' scope
		read -p 'Granulation: ' granulation

		if [[ $granulation -lt $proc ]]; then

			printf 'Cannot pass granulation less than number of proc!\n'
			printf 'Set: granulation = number of proc.\n------------\n'
			mpiexec -n $proc -host localhost python3 src/main.py $scope $proc
		else
			mpiexec -n $proc -host localhost python3 src/main.py $scope $granulation
		fi
	else
		echo 'Try again!'
	fi
fi
