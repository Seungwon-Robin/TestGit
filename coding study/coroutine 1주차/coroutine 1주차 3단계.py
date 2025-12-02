#Coroutine 과제
#3단계
#6
import sys
a = int(input()) #a의 개수만 반복되는 것이다
for i in range(a):
    b = list(map(int, sys.stdin.readline().split()))
    print(sum(b))
#11
while True:
    a,b = map(int, input().split())
    if not a and b==0:
        break
    print(a+b)
#12
while True:
    try:
        a,b = map(int, input().split())
        print(a+b)
    except:
        break