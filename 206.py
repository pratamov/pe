from multiprocessing import Process
from math import sqrt
from decimal import Decimal, getcontext
from re import match

getcontext().prec = 100

lower_bound = int(Decimal(1020304050607080900).sqrt())
upper_bound = int(Decimal(1929394959697989990).sqrt())

def worker(id_, from_, to_):
    for i in range(from_, to_):
        if match(r"1[0-9]2[0-9]3[0-9]4[0-9]5[0-9]6[0-9]7[0-9]8[0-9]9[0-9]0", str(i*i)):
            print('Matched ', i)
            break

if __name__ == '__main__':
    job_count = 1000
    range_ = int((upper_bound - lower_bound) / job_count)
    process = []
    for i in range(job_count):
        from_ = lower_bound + range_*i
        to_ = lower_bound + range_*(i+1)
        p = Process(target=worker, args=(i, from_, to_))
        process.append(p)
    
    for p in process:
        p.start()
    
    for p in process:
        p.join()