from math import sqrt

class Sieve():

    @staticmethod
    def regular_eratosthenes(scope):
        array_of_primes = bytearray(scope + 1)

        for i in range(2,scope + 1):
            if i > sqrt(scope): # optlimalization: chceck only for prime less than sqrt(scope)
                array_of_primes    
            if array_of_primes[i] == 0:

                for j in range(i**2, scope + 1, i):
                    array_of_primes[j] = 1
        lol = []

        for i in range(scope):
            if array_of_primes[i] == 0:
                lol.append(i)

        return array_of_primes

    @staticmethod
    def sieve(left_bound, right_bound):

        sqrt_right_b = int( sqrt(right_bound) )

        scope = right_bound - left_bound + 1
        primes = bytearray(scope)

        primes_on_sqrt = Sieve.regular_eratosthenes(sqrt_right_b)

        for i in range(2, sqrt_right_b + 1):
            if primes_on_sqrt[i] == 0:
                # looking for first number on the scope that is a multiple of prime-i
                first_num_on_scope = int(left_bound/i)*i

                if first_num_on_scope < left_bound:
                    first_num_on_scope += i
                # if first number on the scope is a i-prime than add i-prime to skip it 
                if first_num_on_scope == i:
                    first_num_on_scope += i
                
                for j in range(first_num_on_scope, right_bound + 1, i):
                    primes[j - left_bound] = 1

        primes_as_int = []

        for i in range(scope):
            if primes[i] == 0:
                primes_as_int.append(i + left_bound)

        return primes_as_int

    @staticmethod
    def store_primes(prev_primes, new_primes):
        return prev_primes + new_primes
