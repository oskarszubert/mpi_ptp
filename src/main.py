import sys

from Process_farm import *
from Euler_pi import *

if __name__ == '__main__':
    try:
        begin_at = int(sys.argv[1])
        scope = int(sys.argv[2])
        granulation = int(sys.argv[3]) 
    except:
        print('Did something wrong! ')
        exit()

    ptp = Process_farm()

    pi_num = Euler_pi()

    res = ptp.run(pi_num.compute_subtotals, pi_num.add_subtotals, begin_at, scope, granulation)

    pi = pi_num.calucalte_pi(res)
    print(pi)
