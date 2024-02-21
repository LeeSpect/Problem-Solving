n = int(input()); k = int(input())

if n <= k+60: print(n*1500)
else: print((k+60)*1500 + (n-k-60)*3000)
