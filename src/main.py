import sys

from Process_farm import *
from Euler_pi import *
from Sieve import *
from Time import *  

if __name__ == '__main__':
    try:
        if len(sys.argv) == 4:        
            begin_at = int(sys.argv[1])
            scope = int(sys.argv[2])
            granulation = int(sys.argv[3]) 
            trigger = 1 
            
            if begin_at == 1:
                begin_at += 1       

        if len(sys.argv) == 3:
            scope = int(sys.argv[1])
            granulation = int(sys.argv[2]) 
            trigger = 2
 
    except:
        print('Did something wrong!')
        exit()

    time = Time()

    ptp = Process_farm()
    if trigger == 1:
        prime_nums = Sieve()
        res = []
        time.start()

        res = ptp.run(res, prime_nums.sieve, prime_nums.store_primes, begin_at, scope, granulation)
        time.stop()

        time_as_str =  '{0:8f}'.format(time.result)

        res.sort()
        info_str = 'Found {} primes number.\n'.format(len(res))
        result_filename = ptp.save_to_file(granulation, time_as_str, info_str, res)

        print(info_str + '\n' + 'Time = ' + time_as_str + '[sec].')
        print('Result save into the file: ' + result_filename )


    if trigger == 2:
        pi_num = Euler_pi()
        res = 0
        time.start()
        
        res = ptp.run(res, pi_num.compute_subtotals, pi_num.add_subtotals, 1, scope, granulation)
        time.stop()
        
        time_as_str =  '{0:8f}'.format(time.result)
        pi = pi_num.calucalte_pi(res)
        info_str = 'Found approximation on PI number: '
        result_filename = ptp.save_to_file(granulation, time_as_str, info_str, pi)

        print(info_str + str(pi) + '\n' + 'Time = ' + time_as_str + '[sec].')
        print('Result save into the file: ' + result_filename )
