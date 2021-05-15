n=int(input()) #the number of numbers
list1=[]

def sort(num, n):
    list1.append(num)
    if n==0:
        return
    else:
        while n>0:
            if list1[n-1]>list1[n]:
                temp=list1[n]
                list1[n]=list1[n-1]
                list1[n-1]=temp
            n=n-1
        return

if n<=1000 and n>=1:
    for i in range(n):
        number=int(input())
        sort(number, i)
    for j in range(len(list1)):
        print(list1[j])