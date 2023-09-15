i=1
def evenNumber(i):
    r = i * 2
    yield r 
while True:
    print(evenNumber(i))
    i+=1
