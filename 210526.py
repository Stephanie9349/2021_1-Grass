def backward(num):
    n=0
    while num>0:
        n=n*10+int(num%10)
        num=int(num/10)
    return n

a, b=input().split()
a=backward(int(a))
b=backward(int(b))
print(b) if a<b else print(a)