l = list(map(int, input('Введите числа через пробел:').split()))
n = len(l)
max = 0
count = 0
while count < n:
  if l[count] > max:
    max = l[count]
  count += 1
print(max)  
