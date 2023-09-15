import math
def primefactors(n):
   l=[]
   while n % 2 == 0:
      l.append(2),
      n = n // 2 
   for i in range(3,int(math.sqrt(n))+1,2):
     
      while (n % i == 0):
         l.append(i)
         n = n / i
    
   if n > 2:
      l.append(n)
   return l
n = int(input("Enter the number for calculating the prime factors :\n"))
l=primefactors(n)
d={}
for i in l:
    if i not in d.keys():
        d[i]=l.count(i)
print(d)

