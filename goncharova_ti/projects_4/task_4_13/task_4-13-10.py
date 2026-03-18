l = list(map(int, input('Введите числа через пробел:').split()))
n = len(l)
sum = 0
count = 0
while count < n:
  if count % 2 != 0:
    sum += l[count]
  count += 1
print(sum)  
