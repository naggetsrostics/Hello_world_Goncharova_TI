a,b,c,d = int(input()), int(input()), int(input()), int(input())
max = 0
if a>b:
  max = a
else:
  max =b
if max < c:
  max = c
if max <d:
  max = d
print(max)
