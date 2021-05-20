A=int(input())
B=int(input())
C=int(input())
num=A*B*C
output=[0,0,0,0,0,0,0,0,0,0]
temp=num
for i in range(len(str(num))):
    a=int(temp%10)
    for j in range(10):
        if a==j:
            output[j]+=1
    temp/=10
for k in range(len(output)):
    print(output[k])