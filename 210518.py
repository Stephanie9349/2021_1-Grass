N=int(input())
list1=[]

def printing(list3):
    for i in range(len(list3)):
        print(list3[i])

def sorting(list2):
    list2.sort()
    printing(list2)

if 1<=N and N<=1000000:
    for i in range(N):
        num=int(input())
        list1.append(num)
    sorting(list1)