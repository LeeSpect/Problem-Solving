import sys; input=sys.stdin.readline

def main():
    S=input().rstrip()
    D=input().rstrip()
    len_S,len_D=len(S),len(D)
    l=[]
    pos=[0]
    cnt=0
    for i in range(len_S):
        if S[i]!=D[cnt]:
            cnt=0
        if S[i]!=D[cnt]:
            l.append(S[i])
            pos.append(0)
        else:
            l.append(S[i])
            cnt+=1
            pos.append(cnt)
            if cnt==len_D:
                for _ in range(len_D):
                    l.pop()
                    pos.pop()
            cnt=pos[-1]
    if l:
        print(''.join(l))
    else:
        print('FRULA')

if __name__ == '__main__':
    main()
