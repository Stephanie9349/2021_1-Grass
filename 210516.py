n=int(input())
output=0
number=int(input())
if n<=100 and n>=1:
    for i in range(n):
        output+=int(number%10)
        number/=10
    print(output)