t = int(input())


while(t):
    
    
    n, k = map(int,input().split(" "))
    a = 2**(n-(k-1))+ 2*(k-1)
    print(a)
    
    t-=1
    
