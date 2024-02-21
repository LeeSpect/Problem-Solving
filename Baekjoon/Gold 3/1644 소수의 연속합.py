# ----------------------------------------------------------------------------------------------------
# 틀린 코드: 입력이 1인 경우를 고려하지 않았다.
import sys; input=sys.stdin.readline

def make_prime_list(n):
    prime = [1 for i in range(n+1)]
    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            j = 2
            while j*i <= n:
                prime[j*i] = 0
                j += 1
    l = []
    for i in range(2, n+1):
        if prime[i]:
            l.append(i)
    return l

def find_prime_sum(goal):
    prime_list = make_prime_list(goal)
    point_1, point_2 = 0, 1
    cnt = 0
    total = prime_list[point_1] + prime_list[point_2]
    while 1:
        if point_1 == point_2:
            if goal in prime_list:
                return cnt+1
            else:
                return cnt
        if total <= goal:
            if total == goal:
                cnt += 1
            point_2 += 1
            total += prime_list[point_2]

        elif total > goal:
            total -= prime_list[point_1]
            point_1 += 1

def main():
    goal = int(input())
    print(find_prime_sum(goal))

if __name__=='__main__':
    main()

# ----------------------------------------------------------------------------------------------------
# 틀린 수정 코드: N이 1인 경우 0을 출력하고 exit()하였으나, 입력이 2인 경우를 고려하지 않음.
import sys; input=sys.stdin.readline

def make_prime_list(n):
    prime = [1 for i in range(n+1)]
    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            j = 2
            while j*i <= n:
                prime[j*i] = 0
                j += 1
    l = []
    for i in range(2, n+1):
        if prime[i]:
            l.append(i)
    return l

def find_prime_sum(goal):
    prime_list = make_prime_list(goal)
    point_1, point_2 = 0, 1
    cnt = 0
    total = prime_list[point_1] + prime_list[point_2]
    while 1:
        if point_1 == point_2:
            if goal in prime_list:
                return cnt+1
            else:
                return cnt
        if total <= goal:
            if total == goal:
                cnt += 1
            point_2 += 1
            total += prime_list[point_2]

        elif total > goal:
            total -= prime_list[point_1]
            point_1 += 1

def main():
    goal = int(input())
    if goal == 1:
        print(0)
        exit()
    print(find_prime_sum(goal))

if __name__=='__main__':
    main()

# ----------------------------------------------------------------------------------------------------
# 수정 코드: 입력이 2일 때 1을 출력
import sys; input=sys.stdin.readline

def make_prime_list(n):
    prime = [1 for i in range(n+1)]
    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            j = 2
            while j*i <= n:
                prime[j*i] = 0
                j += 1
    l = []
    for i in range(2, n+1):
        if prime[i]:
            l.append(i)
    return l

def find_prime_sum(goal):
    prime_list = make_prime_list(goal)
    point_1, point_2 = 0, 1
    cnt = 0
    total = prime_list[point_1] + prime_list[point_2]
    while 1:
        if point_1 == point_2:
            if goal in prime_list:
                return cnt+1
            else:
                return cnt
        if total <= goal:
            if total == goal:
                cnt += 1
            point_2 += 1
            total += prime_list[point_2]

        elif total > goal:
            total -= prime_list[point_1]
            point_1 += 1

def main():
    goal = int(input())
    if goal == 1:
        print(0)
        exit()
    if goal == 2:
        print(1)
        exit()
    print(find_prime_sum(goal))

if __name__=='__main__':
    main()
