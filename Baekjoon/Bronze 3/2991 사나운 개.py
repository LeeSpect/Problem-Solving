a1,a2,b1,b2 = map(int, input().split())
l = list(map(int, input().split()))

aa = a1+a2
bb = b1+b2
for i in l:
    bark = 0
    if a1 >= (i%aa) and i%aa != 0:
        bark += 1
    if b1 >= (i%bb) and i%bb != 0:
        bark += 1
    print(bark)
