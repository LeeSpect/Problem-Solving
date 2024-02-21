def switch(x):
    print({1:1, 2:2, 3:3, 4:4, 5:5, 6:4, 7:3, 0:2}.get(x))

n = int(input())
switch(n%8)
