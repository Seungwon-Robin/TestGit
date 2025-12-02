#Coroutine 과제
#4단계
#2
N,X = map(int,input().split())
A = list(map(int,input().split()))
for i in A:
   if i < X:
       print(i,end=' ')
#4
a1 = int(input())
a2=int(input())
a3=int(input())
a4=int(input())
a5=int(input())
a6=int(input())
a7=int(input())
a8=int(input())
a9=int(input())
A = [a1,a2,a3,a4,a5,a6,a7,a8,a9]
b = A.index(max(A))
print(max(A))
print(b+1)
#7
a = []
for i in range(0,28):
   a.append(int(input()))
b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
c = []
for e in b:
    if e not in a:
        c.append(e)
for j in c:
    print(j,end='\n')
#8
a = []
for i in range(0,10):
    b = int(input())
    a.append(b)
c= [i%42 for i in a ]
print(len(set(c))) #set함수는 데이터의 중복된 요소들을 제거해준다

