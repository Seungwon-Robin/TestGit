#1
#clear
#3
numa=0
numb=0
numc=0
numd=0
nume=0
lsta = []
lstb=[]
lstc=[]
lstd=[]
lste=[]
a= input()
b= input()
c= input()
d= input()
e= input()

for i in list(a):
    lsta.append(list(a)[numa])
    numa +=1  
for i in list(b):
    lstb.append(list(b)[numb])
    numb +=1
for i in list(c):
    lstc.append(list(c)[numc])
    numc +=1
for i in list(d):
    lstd.append(list(d)[numd])
    numd +=1
for i in list(e):
    lste.append(list(e)[nume])
    nume +=1
for j in range(0,15):
    if j < len(lsta):
        print(lsta[j], end='')
    if j < len(lstb):
        print(lstb[j], end='')
    if j < len(lstc):
        print(lstc[j], end='')
    if j < len(lstd):
        print(lstd[j], end='')
    if j < len(lste):
        print(lste[j], end='')