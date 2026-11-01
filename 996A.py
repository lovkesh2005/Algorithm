n = int(input())

count = 0

if(n>=100):
    count = count + n//100
    n = n%100
if(n>=20):
    count = count + n//20 
    n = n%20
if(n>=10):
    count = count + n//10
    n = n%10
if(n>=5):
    count = count + n//5
    n = n%5
if(n<5):
    count = count + n
    if n!= 0:
        n = n/n-1
    else:
        n = 0
    
     
        
print(count)
    
    