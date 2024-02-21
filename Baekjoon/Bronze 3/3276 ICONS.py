n = int(input())
if n**0.5%1 == 0:
    print(int(n**0.5), int(n**0.5))
elif n**0.5%1 < 0.5:
    print(int(n**0.5//1), int(n**0.5//1+1))
else:
    print(int(n**0.5//1+1), int(n**0.5//1+1))
