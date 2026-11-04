t = int(input())

for _ in range(t):
    n = int(input())
    s = input().lower()

    res = s[0]

    for i in range(1, n):
        if s[i] != s[i - 1]:
            res += s[i]

    print("YES" if res == "meow" else "NO")