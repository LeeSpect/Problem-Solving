a, b = map(int, input().split())

lists = list(input().split())
new_lists = ''

for i in lists:
    if int(i) < b:
        new_lists += str(i)
        new_lists += ' '

print(new_lists)
