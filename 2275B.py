t = int(input())

while(t):
    n = int(input())
    s = input().strip()
    l = len(s)
    a = []      
    printed = set()

    for i in range(len(s)):
        if s[i] == '1':
            a.append(i+1)
        elif s[i] == '2':
            if a:
                c = a.pop()    
                printed.add(c)
            else:
                c = i+1        
                printed.add(c)
        elif s[i] == '3':
            printed.add(i+1)


    unprinted = [x for x in range(1, n+1) if x not in printed]
    print(len(unprinted))
    if unprinted:
        print(*unprinted)

    t -= 1
