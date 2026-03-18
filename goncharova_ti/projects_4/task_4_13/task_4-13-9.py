l = list(map(int, input('Введите числа через пробел:').split()))
n = len(l)
nechet = 0
count = 0
while count < n:
  if l[count] % 2 != 0 :
    nechet += l[count]
  count += 1
print(nechet)  
