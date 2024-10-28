cnt = 0
numbers = []

while True:
    if cnt == 9:
        break
    n = int(input())
    numbers.append(n)
    cnt += 1

print(max(numbers))
print(numbers.index(max(numbers))+1)
