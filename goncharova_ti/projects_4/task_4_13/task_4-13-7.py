l = list(map(int, input('Введите числа через пробел:').split()))
n = len(l)
sum = 0
count = 0
while count < n:
  sum += l[count]
  count += 1
print(count/n)  
