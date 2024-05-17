#MASTER LIST
#1
el=20
d=[]
for i in range(el + 1):
    if i % 2 == 0:
        d.append(i)
print(d)
#2
lis=[1,2,3,4,5,6,77]
list=[]
for i in lis:
    list.append(str(i))
print(list)
#3
l=[]
j=input('entrer une liste: ')
for i in j:
    l.append(i.upper())
print(l)
#4
j=input('entrer une liste: ')
n = [elem for index, elem in enumerate(j) if index % 3 == 0]
print(n)
#5
j=input('entrer une liste: ')
n = [tuple(j[i:i+3]) for i in range(0, len(j), 3)]
print(n)
#6
j = input('Antre yon lis: ')
lis = j.split(',')
lis = [eleman.strip() for eleman in lis]
n = list(set(lis))
print(n)
#7
j1=input('entrer une liste: ')
j2=input('entrer une liste: ')
l1 = []
l2 = []
l1.append(j1)
l2.append(j2)
n = [l1[i] for i in range(len(l1)) if l1[i] == l2[i]]
print(n)
#8
j1=input('entrer une liste: ')
j2=input('entrer une liste: ')
l1 = []
l2 = []
l1.append(j1)
l2.append(j2)
n = list(set(l1) ^ set(l2))
print(n)
#9
dik = {'kle1': 'valè1', 'kle2': 'valè2', 'kle3': 'valè3'}
keys = list(dik.keys())
value = list(dik.values())
print(keys)
print(value)
#10
l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]
l3 = [7, 8, 9, 10, 11]
som = list(set(l1) | set(l2) | set(l3))
print(som)