while 1:
    l = list(map(int, input().split()))
    if l[0] == l[1] == 0: break
    else:
        l.sort()
        a, b = str(l[0]), str(l[1])
        carry = 0
        post_carry = 0
        for i in range(1, len(b) + 1):
            if len(a) >= i:          
                if (int(a[-i]) + int(b[-i]) + post_carry) // 10:
                    carry += 1
                    post_carry = 1
                else: post_carry = 0
            else:
                if (int(b[-i]) + post_carry) // 10:
                    carry += 1
                    post_carry = 1
                else:
                    break
        print(carry)
# 99 1의 경우에 carry 처리를 post_carry를 통해 
