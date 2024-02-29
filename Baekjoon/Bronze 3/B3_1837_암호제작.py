def prime_list(k):
    sieve = [False,False] + [True]*k

    # k의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(k)까지 검사
    m = int(k ** 0.5)
    for i in range(2, m+1):
        if sieve[i]:    # i가 소수인 경우
            for j in range(i+i, k, i): # i이후 i의 배수들을 False로 판정
                sieve[j] = False
    return [i for i in range(2, k) if sieve[i]]

p,k = map(int, input().split())
kpl = prime_list(k)
c = 0; ans = 0
for i in kpl:
    if p%i == 0:
        ans = i
        c=1
        break
print('GOOD' if c==0 else f'BAD {ans}')
