# from math import gcd, factorial, floor, ceil
# from fractions import Fraction
# import operator as op
# from functools import reduce
# def nCr(n, r):
# 	r = min(r,n-r)
# 	numer = reduce(op.mul, range(n,n-r,-1), 1)
# 	denom = reduce(op.mul, range(1,r+1), 1)
  
# T = int(input().strip())
# for _ in range(T):
# 	A, H, L1, L2, M, C = tuple(map(int,input().strip()))
# 	special_needed, L = ceil((H-M*A)/C), Fraction(L1,L2)
    
# 	count = Fraction(0)
# 	for k in range(special_needed,M+1):
# 		count += nCr(M,K)*L**K*(1-L)**(M-K)
        
#     p1,p2= count.numer, count.denom
#     if p1==0:
# 		print('RIP')
#     else:
# 		_ =gcd(p1,p2)
# 		print('{}/{}'.format(p1//_,p2//_))