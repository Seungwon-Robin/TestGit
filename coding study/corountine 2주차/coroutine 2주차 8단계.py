#coroutine 8단계
#1
a,b = input().split()
b = int(b)
result = []
c=[]
for i in range(0, len(list(a))):
    if list(a)[i]=='A' and b>10:
        result.append(10)    
    elif list(a)[i]=='B' and b>11:
        result.append(11)
    elif list(a)[i]=='C' and b>12:
        result.append(12)
    elif list(a)[i]=='D' and b>13:
        result.append(13)
    elif list(a)[i]=='E' and b>14:
        result.append(14)
    elif list(a)[i]=='F' and b>15:
        result.append(15)
    elif list(a)[i]=='G' and b>16:
        result.append(16)
    elif list(a)[i]=='H' and b>17:
        result.append(17)
    elif list(a)[i]=='I' and b>18:
        result.append(18)
    elif list(a)[i]=='J' and b>19:
        result.append(19)
    elif list(a)[i]=='K' and b>20:
        result.append(20)
    elif list(a)[i]=='L' and b>21:
        result.append(21)
    elif list(a)[i]=='M' and b>22:
        result.append(22)
    elif list(a)[i]=='N' and b>23:
        result.append(23)
    elif list(a)[i]=='O' and b>24:
        result.append(24)
    elif list(a)[i]=='P' and b>25:
        result.append(25)
    elif list(a)[i]=='Q' and b>26:
        result.append(26)
    elif list(a)[i]=='R' and b>27:
        result.append(27)
    elif list(a)[i]=='S' and b>28:
        result.append(28)
    elif list(a)[i]=='T' and b>29:
        result.append(29)
    elif list(a)[i]=='U' and b>30:
        result.append(30)
    elif list(a)[i]=='V' and b>31:
        result.append(31)
    elif list(a)[i]=='W' and b>32:
        result.append(32)
    elif list(a)[i]=='X' and b>33:
        result.append(33)
    elif list(a)[i]=='Y' and b>34:
        result.append(34)
    elif list(a)[i]=='Z' and b>35:
        result.append(35)
    elif list(a)[i]=='1' and b>1:
        result.append(1)
    elif list(a)[i]=='2' and b>2:
        result.append(2)
    elif list(a)[i]=='3' and b>3 :
        result.append(3)
    elif list(a)[i]=='4' and b>4:
        result.append(4)
    elif list(a)[i]=='5' and b>5:
        result.append(5)
    elif list(a)[i]=='6' and b>6:
        result.append(6)
    elif list(a)[i]=='7' and b>7:
        result.append(7)
    elif list(a)[i]=='8' and b>8:
        result.append(8)
    elif list(a)[i]=='9' and b>9:
        result.append(9)
for j in range(0, len(result)):
    c.append(result[j]*(b**(len(result)-(j+1))))
print(sum(c))
#1 -answer
a, b = input().split()
b = int(b)
result = 0

# 알파벳 대문자에 대한 처리를 딕셔너리에 저장
alpha_values = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19,
                'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29,
                'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}

# 입력된 수를 거꾸로 반전하여 처리하기 위해 문자열로 변환 후 거꾸로 읽음
a = list(a)
a.reverse()

# 각 자릿수마다 진법에 맞게 변환하여 10진법으로 합산
for i in range(len(a)):
    if a[i] in alpha_values:
        result += alpha_values[a[i]] * (b ** i)
    else:
        result += int(a[i]) * (b ** i)

print(result)

#3