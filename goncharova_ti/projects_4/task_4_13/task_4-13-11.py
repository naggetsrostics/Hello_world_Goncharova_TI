l = list(map(int, input('Введите числа через пробел:').split()))
n = len(l)
sum = 0
count = 0
num = 0
while count < n:
  if count % 2 == 0 :
    sum += l[count]
    cum += 1
  count += 1
sr = sum / num
print(sr)  
