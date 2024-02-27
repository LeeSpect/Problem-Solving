n = int(input())
for _ in range(n):
    string = input().lower()

    flag = True
    for i in range(len(string)):
        if string[i] != string[len(string)-i-1]:
            flag = False
            break
    
    print("Yes" if flag else "No")