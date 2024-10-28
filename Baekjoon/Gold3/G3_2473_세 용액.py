# ----------------------------------------------------------------------------------------------------
# 틀린 코드: 단순 투 포인터로만 구현한다면 목표 값을 구하지 못 할 수도 있다.
import sys; input=sys.stdin.readline

def main():
    N = int(input())
    l = list(map(int, input().split()))
    l.sort()
    a, b, c = 0, N//2, N-1
    ans_a, ans_b, ans_c = a, b, c
    min_abs_total = float('inf')
    while 0 <= a and c < N:
        total = l[a] + l[b] + l[c]
        # print(total, l[a], l[b], l[c])
        if abs(total) > min_abs_total:
            break
        else:
            ans_a, ans_b, ans_c = a, b, c
            min_abs_total = abs(total)
        if total < 0:
            if a+1 == b == c-1:
                c += 1
            elif a+1 == b:
                b = (b+c)//2
            else:
                a = (a+b)//2
        else:
            if a+1 == b == c-1:
                a -=1
            elif b+1 == c:
                b = (a+b+1)//2
            else:
                c = (b+c+1)//2
    print(l[ans_a], l[ans_b], l[ans_c])

if __name__=='__main__':
    main()

# ----------------------------------------------------------------------------------------------------
# 틀린 수정 코드: 예외 처리를 통해 더 자세히 확인하려 했지만, 모든 경우의 수를 확인하지 않는 이상 목표 값을 찾을 수 없다는 것은 동일하다.
import sys; input=sys.stdin.readline

def main():
    N = int(input())
    l = list(map(int, input().split()))
    l.sort()
    a, b, c = 0, (N-1)//2, N-1
    ans_a, ans_b, ans_c = a, b, c
    min_abs_total = float('inf')
    condition = ''
    while a != b != c:
        total = l[a] + l[b] + l[c]
        if abs(total) < min_abs_total:
            ans_a, ans_b, ans_c = a, b, c
            min_abs_total = abs(total)
        print(l[a], l[b], l[c])
        if total < 0:
            if a+1 == b and condition == 'left':
                break
            if b + 1 == c or condition == 'left':
                a += 1
                condition = ''
            else:
                b += 1
                condition = 'right'
        elif total > 0:
            if b+1 == c and condition == 'right':
                break
            if b - 1 == a or condition == 'right':
                c -= 1
                condition = ''
            else:
                b -= 1
                condition = 'left'
        else:
            break
    print(l[ans_a], l[ans_b], l[ans_c])

if __name__=='__main__':
    main()

# ----------------------------------------------------------------------------------------------------
# 수정 코드: 리스트 정렬 후 '값을 하나 지정하고 그 값 이후의 범위에서 정답고 ㅏ가까운 수를 찾아내는 과정'을 모든 요소에 걸쳐 시행한다.
import sys; input=sys.stdin.readline

def find_zero(l, i, N):
    start, end = i+1, N-1
    total_final = float('inf')
    b_final, c_final = 0, 0
    while start < end:
        total = l[i] + l[start] + l[end]
        if abs(total) < total_final:
            total_final = abs(total)
            b_final, c_final = start, end
        if total < 0:
            start += 1
        elif total > 0:
            end -= 1
        else:
            break
    return total_final, b_final, c_final

def main():
    N = int(input())
    l = list(map(int, input().split()))
    l.sort()
    ans = float('inf')
    ans_a, ans_b, ans_c = 0, 0, 0
    for i in range(N-2):
        total_final, b, c = find_zero(l, i, N)
        if total_final == 0:
            print(l[i], l[b], l[c])
            exit()
        if total_final < ans:
            ans = total_final
            ans_a, ans_b, ans_c = i, b, c
    print(l[ans_a], l[ans_b], l[ans_c])

if __name__=='__main__':
    main()
