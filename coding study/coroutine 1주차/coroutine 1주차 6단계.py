#Coroutine
#6단계
#4
text = input()
a = []
for i in text:
    a.append(i)
if a == a[::-1]:
    print(1)
else :
    print(0)
#5
#text = input()
#upper_text=text.upper()
#from collections import Counter
#a =[]
#for i in upper_text:
#    a.append(i)
#counter = Counter(a)
#most_common_items = counter.most_common()
#most_common_items2 =  [t[1:]for t in most_common_items]
#print(most_common_items2)
#max_frequency = most_common_items[0][1]
#print(max_frequency) #튜플 자료형
#if most_common_items2[0] == most_common_items[1] :
#    print('?')
#else:
#    print(counter.most_common(1)[0][0])
#6 import string
list1 = []
count=''
let=input()
if 'lj' in let:
    for _ in range(let.count('lj')):
        list1.append('1')
if 'c=' in let:
    for _ in range(let.count('c=')):
        list1.append('2')
if 'c-' in let:
    for _ in range(let.count('c-')):
        list1.append('3')
if 'z=' in let:
    for _ in range(let.count('z=')):
        list1.append('8')
if 'dz=' in let:
    for _ in range(let.count('dz=')):
         list1.append('4')
if 'd-' in let:
    for _ in range(let.count('d-')):
        list1.append('5') 
if 'nj' in let:
    for _ in range(let.count('nj')):
        list1.append('6')
if 's=' in let:
    for _ in range(let.count('s=')):
        list1.append('7')
exclusions = ['s=', 'nj', 'd-', 'dz=', 'z=', 'c-', 'c=', 'lj']
index = 0
while index < len(let):
    # 현재 위치부터 가능한 모든 예외 문자열들을 확인합니다.
    found = False
    for exclusion in exclusions:
        if let[index:].startswith(exclusion): #let[index:] let문자열을 슬라이싱하여 인덱싱한다.
            found = True #startswitch(exclusion): slicing된 exclusion string을 체크한다.
            index += len(exclusion)
            break
    if not found:
        list1.append(0)
        index += 1
if '4'in list1 and'8' in list1:
    b=list1.count('4')
    for i in range(b):
        list1.remove('8')   
a =len(list1) 
print(a)