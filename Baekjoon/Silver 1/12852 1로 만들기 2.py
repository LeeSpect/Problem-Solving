import sys; input=sys.stdin.readline

def make_one(l):
    visited=set()
    visited.add(l[0][0][0])
    while 1:
        l.append([])
        while l[-2]:
            k=l[-2].pop()
            if k[-1]%3==0:
                divide_by_3=k[-1]//3
                if divide_by_3==1:
                    print(len(l)-1)
                    k.append(1)
                    print(*k)
                    return
                if divide_by_3 not in visited:
                    visited.add(divide_by_3)
                    l[-1].append(k+[divide_by_3])
            if k[-1]%2==0:
                divide_by_2=k[-1]//2
                if divide_by_2==1:
                    print(len(l)-1)
                    k.append(1)
                    print(*k)
                    return
                if divide_by_2 not in visited:
                    visited.add(divide_by_2)
                    l[-1].append(k+[divide_by_2])
            if k[-1]-1==1:
                print(len(l)-1)
                k.append(1)
                print(*k)
                return
            if k[-1]-1 not in visited:
                visited.add(k[-1]-1)
                l[-1].append(k+[k[-1]-1])

def main():
    N=int(input())
    if N==1:
        print(0)
        print(1)
        exit()
    l=[[[N]]]
    make_one(l)

if __name__=='__main__':
    main()
