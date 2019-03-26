from time import sleep
from mpi4py import MPI


class Process_farm:

    def __init__(self):
        self.comm = MPI.COMM_WORLD
        self.size = self.comm.Get_size()
        self.rank = self.comm.Get_rank()
        self.status = MPI.Status()

    def run(self, compute_function, result_function, begin_at, scope, granulation):
        if self.rank == 0:   
            partition_array = Process_farm.create_partition_array(begin_at, scope + 1, granulation -1 )
            result = self.master(result_function, partition_array , granulation)
            return result
        else:
            self.slave(compute_function)

    def master(self, result_function, partition_array, granulation):
        number = 10
        work = granulation
        result  = []

        # send first jobs 
        for proc in range(1,self.size):
            data = partition_array[ proc - 1 ], partition_array[ proc ]
            self.comm.send(data, dest=proc)

            work -= 1

        while work:
            work -= 1

            data_from_slave = self.comm.recv(source=MPI.ANY_SOURCE, status=self.status)
            result = result_function(result, data_from_slave )

            data = partition_array[ proc ], partition_array[ proc + 1 ]
            source = self.status.Get_source()       
            self.comm.send(data, dest=source)
            proc += 1


        # recv rest data from slaves
        for proc in range(1,self.size):
            data_from_slave = self.comm.recv(source=MPI.ANY_SOURCE)
            result = result_function(result, data_from_slave )

        # end all slaves
        for proc in range(1,self.size):
            end_status = -1
            self.comm.send(end_status, dest=proc)


        return result


    def slave(self, function):
        while True:
            data = self.comm.recv(source=0)

            if data == -1:
                exit()
            else:
                data = function(data)
                self.comm.send(data, dest = 0)


    @staticmethod
    def create_partition_array(begin_at, scope, granulation):
        partition_array = []

        if granulation == 0:
            granulation = 1

        num_of_ele_in_one_part = (scope - begin_at) // granulation
        for i in range(granulation + 1):
            partition_array.append(begin_at)
            begin_at += num_of_ele_in_one_part

        partition_array.append(scope)

        return partition_array
