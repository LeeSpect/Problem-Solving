string = input()
if '7' not in string and int(string) % 7 != 0:
    print(0)
elif '7' not in string and int(string) % 7 == 0:
    print(1)
elif '7' in string and int(string) % 7 != 0:
    print(2)
else:
    print(3)