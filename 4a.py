str='Hello'#string is an iterable
a=len(str)
l=[]
for i in range(a):
    l.append(str[i])
print(type(l))
print(l)
