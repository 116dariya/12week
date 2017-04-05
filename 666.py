from multiprocessing import Pool

def summ(t):
	k , l = t
	s = 0
	for i in range(k , l + 1 ):
		s = s + i
	return s

if __name__ == '__main__':
    pool = Pool(processes=2)
    n = 100
    l = pool.map(summ, [(0, n//2),(((n//2)+1),n)])
    print(l)
    s = 0
    for i in l:
    	s = s + i
    print(s)
    