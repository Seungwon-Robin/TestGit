#Coroutine
#5단계
#1
text = input()
index = int(input())
print(text[index-1])
#4
a = input()
print(ord(a)) #ord() 아스키코드에 대한 함수가 존재
#5
num = int(input())
print(sum(map(int,[*input()]))) #input()을 가변인자로 설정하여 위에 num의 개수만큼 입력하면 된다
#9
List = []

inList = list(str(input()))

num1 = int(inList[2])*100 + int(inList[1])*10 + int(inList[0])
num2 = int(inList[6])*100 + int(inList[5])*10 + int(inList[4])

List.append(num1)
List.append(num2)

print(max(List))
