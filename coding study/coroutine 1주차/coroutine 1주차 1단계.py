#Coroutine 과제
#1
print('Hello World!')
#6 map함수(,): 앞자리에는 각요소에 적용할 함수, 뒷자리에는 앞의 함수가 적용될 객체 \n split: 입력시에 띄어쓰기로 숫자를 input하기 위해 작성
A,B = map(int, input().split())
1<=A,B<=10000
print(f"{A+B}\n{A-B}\n{A*B}\n{A//B}\n{A%B}")
#9
a,b,c= map(int, input().split())
2<=a,b,c<=10000
print(f"{(a+b)%c}\n{((a%c)+(b%c))%c}\n{(a*b)%c}\n{((a%c)*(b%c))%c}")
#10
num1 = int(input())
num2 = []
Num1 = int(input())
Num2 = []

while Num1 != 0: 
    num2.append(Num1 % 10)  #1의 자리수가 num2 배열에 들어간다
    Num1 = Num1 // 10       #10으로 나누어서 끝 자리를 버린다
num3 = num1*num2[0]*1       #Num1의 1의 자리수의 곱셈
num4 = num1*num2[1]*10      #Num1의 10의 자리수의 곱셈
num5 = num1*num2[2]*100     #Num1의 100의 자리수의 곱셈
num6 = num3+num4+num5       #각 곱셈들의 합 = num1*Num1
print(num3)
print(num4//10)
print(num5//100)
print(num6)