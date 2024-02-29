import sys

while 1:
    s = sys.stdin.readline().rstrip().lower()
    if s=='#': break
    ans=0
    l=['a','e','i','o','u']
    for i in range(len(s)):
        if s[i] in l:
            ans+=1
    print(ans)
