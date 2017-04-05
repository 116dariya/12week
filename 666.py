from multiprocessing import Pool


def f(j):
	q , w = j
	s = 1
	for item in range(q , w + 1):
		
		s = item * s
	return s


if __name__ == '__main__':
    pool = Pool(processes=4)
    n = 5
    l = pool.map(f, [(1, n // 2), ( n// 2 + 1, n )])
    print(l)
    m = 1
    for i in l:
    	m = m * i
    print(m)
    
    # i = 2
    # for item in l:
    # 	if item == True:
    # 		print(i)
    # 	i = i + 1
    #print(l)
    #print(primes)