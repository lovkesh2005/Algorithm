s = input()

a = []
for i in range(len(s)):
    if s[i] != '+':
        a.append(int(s[i]))
    
a.sort()
print("+".join(map(str,a)))