import sys

from Process_farm import *
from Euler_pi import *
from Sieve import *

if __name__ == '__main__':
    try:
        begin_at = int(sys.argv[1])
        scope = int(sys.argv[2])
        granulation = int(sys.argv[3]) 
    except:
        print('Did something wrong! ')
        exit()

    ptp = Process_farm()

    # pi_num = Euler_pi()
    prime_nums = Sieve()

    # res = ptp.run(pi_num.compute_subtotals, pi_num.add_subtotals, begin_at, scope, granulation)

    # pi = pi_num.calucalte_pi(res)

    res = ptp.run(prime_nums.sieve, prime_nums.store_primes, begin_at, scope, granulation)
    # print(pi)

    res.sort()
    for i in res:
        print(i)
