k = int(input())

p = 25 + k/100
if p < 100: print('100.00')
elif p > 2000: print('2000.00')
else: print(f'{p:.2f}')
