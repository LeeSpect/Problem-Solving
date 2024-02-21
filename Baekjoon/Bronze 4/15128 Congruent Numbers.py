# 34 15128 Congruent Numbers.py

l = list(map(int, input().split()))
area = 1/2 * l[0]/l[1] * l[2]/l[3]
if area%1 == 0:
    print(1)
else:
    print(0)
