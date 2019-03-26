import sys

from Process_farm import *
from Euler_pi import *
from Sieve import *

if __name__ == '__main__':
    try:
        begin_at = int(sys.argv[1])
        scope = int(sys.argv[2])
        granulation = int(sys.argv[3]) 
        if len(sys.argv) == 5:
            trigger = int(sys.argv[4])
        else:
            trigger = 1
    except:
        print('Did something wrong!')
        exit()

    ptp = Process_farm()
    if trigger == 1:
        prime_nums = Sieve()
        res = []
        res = ptp.run(res, prime_nums.sieve, prime_nums.store_primes, begin_at, scope, granulation)
        res.sort()
        for i in res:
            print(i)

    if trigger == 2:
        pi_num = Euler_pi()
        res = 0
        res = ptp.run(res, pi_num.compute_subtotals, pi_num.add_subtotals, begin_at, scope, granulation)
        pi = pi_num.calucalte_pi(res)
        print(pi)

