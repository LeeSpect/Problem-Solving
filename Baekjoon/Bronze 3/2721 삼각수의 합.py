n = int(input())

for _ in range(n):
    t = int(input())
    print(int(sum([k*(k+1)*(k+2)*0.5 for k in range(1, t+1)])))   
