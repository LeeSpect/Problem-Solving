n,m,k = map(int, input().split())
# 팀 수 구하기
team = 0
if n >= 2*m: 
    team = m
else:
    team = int(0.5*n)

# 팀 짜고 남은 사람들
lost = n+m - team*3

# 팀 짜고 남은 사람들이 k보다 많을 때
if lost >= k:
    print(team)
else:
    print(team - (k-lost)//3 - bool((k-lost)%3))
