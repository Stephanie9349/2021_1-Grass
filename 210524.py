a=[]
def solve(a):
    ans = 0
    for i in range(len(a)):
        ans+=a[i]
    return ans
n=int(input())
for i in range(n):
    b=int(input())
    a.append(b)
solve(a)