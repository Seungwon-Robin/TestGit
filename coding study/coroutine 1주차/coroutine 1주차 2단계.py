#Coroutine 과제
#2단계
#3
year = int(input())
if year%4 == 0: 
    if year%100 != 0: 
        print('1')    
    elif year%400 == 0:
        print('1')
    else :  #4의 배수이면서 100의 배수인 정수가 출력
        print('0')
else:   #애초에 4의 배수가 아닌 것 출력
    print('0')

#5
hour, minute = map(int, input().split())
0<=hour<=23, 0<=minute<=59
if minute>=45:
    print(hour,minute-45)
else:
    if hour ==0:
        print(23,60-(45-minute))
    else :
        print(hour-1,60-(45-minute))