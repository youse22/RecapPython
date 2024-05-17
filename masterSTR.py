#Master STR
#1
var=input('entrer la phrase: ')
print(var.lower())
2
print(var.split())
3
print(var.title())
4
print(''.join([mot[0] for mot in var.split()]))
5
print(var.replace('a','@'))
6
v=var[1:] + var[0]
print(v.upper())
7
print(var.find('a'))
8
t=0
for i in range (len(var)):
    if var[i]== 'a' or var[i]=='A':
        t+=1
print(t)
9
var=var.replace(' ','')
for i in range(len(var)):
    if var[i] == "a":
        l=[]
        l.append(i)
        print(l)
10
v=var.replace(" ","")
k=len(v)
print(v+str(k))







