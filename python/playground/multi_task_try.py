print('*************** Multiprocessing Process ***********************')
from multiprocessing import Process
import os

def run_proc(name):
    print('Child process %s (%s)' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process is %s' % os.getpid())

    p = Process(target = run_proc, args = ('test',))
    print('Child process will start;')
    p.start()
    p.join()
    print('Child process ended')

print('************ Multiprocessing POOL ******************')

def test_delay(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %.2f seconds' % (name, (end - start)))

if __name__ == '__main__':
    from multiprocessing import Pool
    import time, random

    print('Parent process is %s' % os.getpid())
    pool_size = 2
    p = Pool(pool_size)
    for i in range(pool_size):
        p.apply_async(test_delay, args = (i,)) 

    print('Iteration Ended')

    p.close()
    p.join()
    print('All set!')

print('************* Subprocess ********************')

if __name__ == '__main__':
    import subprocess

    print('nslookup www.python.org')

    r = subprocess.call(['nslookup', 'www.python.org'])

    print('Exit code:', r)
