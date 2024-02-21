while True:
    n = input()
    if n == '0': break
    else:
        nlen = len(n)
        e = nlen+1 #여백 갯수
        e += nlen*3 #숫자들
        e -= n.count('1')
        e += n.count('0')
    print(e)
