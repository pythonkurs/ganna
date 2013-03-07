from collections import Counter
from multiprocessing import *
from IPython.parallel import Client
import sys
from time import time

# Define function
def factorize(n):
    if n < 2:
        return []
    factors = []
    p = 2
    while True:
        if n == 1:
            return factors
        r = n % p
        if r == 0:
            factors.append(p)
            n = n / p
        elif p * p >= n:
            factors.append(n)
            return factors
        elif p > 2:
            p += 2
        else:
            p += 1



if __name__ == "__main__":
	start = time()
	
	if sys.argv[-1] == '-m':
		n_p = cpu_count()
		pool=Pool(processes=n_p)
		results=pool.map(factorize, xrange(2, 500001), chunksize=1000)
		
	if sys.argv[-1] == '-s':
		results=[]
		for i in xrange(2, 500001):
			results.append(factorize(i))
	
	if sys.argv[-1] == '-i':
		cli = Client()
		cli2 = cli[:]
		@cli2.parallel(block=True)
		def factorize2(n):
		    if n < 2:
		        return []
		    factors = []
		    p = 2
		    while True:
		        if n == 1:
		            return factors
		        r = n % p
		        if r == 0:
		            factors.append(p)
		            n = n / p
		        elif p * p >= n:
		            factors.append(n)
		            return factors
		        elif p > 2:
		            p += 2
		        else:
		            p += 1
		results = factorize2.map(xrange(2, 500001))
		
	final=[]
	for i in range(0,len(results)):
		final.append(len(list(set(results[i]))))
	print(Counter(final))	
	ttime= time() - start
	print "Time: " + str(ttime)