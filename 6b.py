l=[1,2,3,4,5,63,4,5,7,2,2,3]
a=[]
n=len(l)
for i in range(n):
    if l[i] not in a:
        a.append(l[i])
a.sort()
print(a)
