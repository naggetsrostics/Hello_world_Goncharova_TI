l = list(map(int, input('Введите числа через пробел:').split()))
n = len(l)
plus = 0
count = 0
while count < n:
  if l[count] > 0:
    plus += 1
  count += 1
print(plus)  
