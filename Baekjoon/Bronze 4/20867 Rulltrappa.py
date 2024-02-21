m,s,g = map(float, input().split())
a,b = map(float, input().split())
l,r = map(float, input().split())

l_wait = l/a; r_wait = r/b
l_time = (m/g)+l_wait; r_time = (m/s)+r_wait
if l_time < r_time:
    print('friskus')
else: print('latmask')
