l = [input() for i in range(6)]
if l.count('W') >= 5:
    print(1)
elif l.count('W') >= 3:
    print(2)
elif l.count('W') >= 1:
    print(3)
else:
    print(-1)
