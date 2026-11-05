k, n, w = map(int,input().split(" "))

a = 0
for i in range(1,w+1):
    
    a += i*k
    
if (a-n) >= 0:
    print(a-n)
else:
    print(0)
