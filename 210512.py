def fac(n):
    if n<=1:
        return 1
    return n*fac(n-1)

N=int(input())
if 0<=N or N<=12:
    print(fac(N))