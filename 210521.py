a, b=input().split()
b2=(int(b)+15)%60
if b2<int(b):
    a2=int(a)
else:
    a2=(int(a)+23)%24
print(a2, b2)