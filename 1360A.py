t = int(input())


while(t):
    
    a,b = map(int,input().split(" "))
    
    ans = (max(2*min(a,b),max(a,b)))**2
    
    print(ans)
    

    t -= 1
    