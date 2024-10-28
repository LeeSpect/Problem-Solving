D,H,W = map(int, input().split())

print(int(((D**2)*H**2/(H**2+W**2))**(1/2)), int(((D**2)*W**2/(H**2+W**2))**(1/2)))

# C^2 = A^2+b^2
