name = input('Введите имя исследователя: ')
data = input('Дата эксперимента: ')
name_of_experiment = input('Название эксперимента: ')
conclusion = input('Результат:')
c1 = '| ФИО исследователя: ' + name
c2 = '| Дата             : ' + data
c3 = '| Эксперимент      : ' + name_of_experiment
with open("C:/Users/tanya/OneDrive/Desktop/journal.txt", 'w', encoding='utf-8') as f:
  print('+----------------------------------------------------------------------+\n| Электронный лабораторный журнал                                      |\n+----------------------------------------------------------------------+', file=f)
  print(c1+ ' '*(71-len(c1))+ '|', sep='', file=f)
  print(c2+ ' '*(71-len(c2))+ '|', sep='', file=f)                    
  print(c3+ ' '*(71-len(c3))+ '|', sep='', file=f)
  print('+----------------------------------------------------------------------+', file=f)
  print('| Вывод:' + 63*' ', '|', sep='', file=f)

  conclusion = conclusion.split()
  while len(conclusion) >= 4:
      line = ' '.join(conclusion[:5])
      print(f'| {line}' + (69-len(line))*' ' + '|', file=f)
      conclusion = conclusion[5:]
  print(f'| {' '.join(conclusion)}' + (69-len(conclusion))*' ' + '|', file=f)
  print('+----------------------------------------------------------------------+', file=f)
