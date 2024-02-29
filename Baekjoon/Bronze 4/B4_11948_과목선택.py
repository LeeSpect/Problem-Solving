A=int(input()); B=int(input()); C=int(input()); D=int(input()); E=int(input()); F=int(input())
l1 = [A,B,C,D]; l1.pop(l1.index(min(l1)))
l2 = [E,F]
print(sum(l1)+max(l2))
