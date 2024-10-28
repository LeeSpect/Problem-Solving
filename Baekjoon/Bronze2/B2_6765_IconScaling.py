import sys
input = sys.stdin.readline

def scale_icon(k):
    icon = ["*x*", " xx", "* *"]
    for line in icon:
        scaled_line = ''.join(char * k for char in line)
        for _ in range(k):
            print(scaled_line)

k = int(input().strip())
scale_icon(k)
