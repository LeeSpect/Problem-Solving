def odd(n):
    if n == 1:
        return 2
    else:
        return odd(n-2) + n + 1

def even(n):
    if n == 2:
        return 4
    else:
        return even(n-2) + n + 1

n = int(input())
if n%2 == 1:
    print(odd(n))
else:
    print(even(n))
