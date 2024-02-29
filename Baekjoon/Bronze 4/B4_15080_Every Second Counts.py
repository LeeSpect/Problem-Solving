# 33 15080 Every Second Counts.py

l = list(map(int, input().split(' : ')))
l2 = list(map(int, input().split(' : ')))

s1 = l[0]*3600 + l[1]*60 + l[2]
s2 = l2[0]*3600 + l2[1]*60 + l2[2]

if s2-s1 >= 0:
    print(s2-s1)
else:
    print(23*3600+59*60+60+s2-s1)
