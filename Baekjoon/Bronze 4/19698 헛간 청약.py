n,w,h,l = map(int, input().split())

wl = w//l; hl = h//l
whl = wl*hl
print(n if n<=whl else whl)
