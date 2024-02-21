def F(x):
    x = str(x)
    return int(x[0]) * len(x)

n = F(int(input()))
for i in range(10000000):
    if n == F(n):
        print('FA')
        break
    else:
        n = F(n)
