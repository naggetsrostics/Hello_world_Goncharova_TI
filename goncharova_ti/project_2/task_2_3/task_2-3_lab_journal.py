name = input('Введите имя исследователя: ')
data = input('Дата эксперимента: ')
name_of_experiment = input('Название эксперимента: ')
conclusion = input('Результат:')
c1 = '| ФИО исследователя: ' + name
c2 = '| Дата             : ' + data
c3 = '| Эксперимент      : ' + name_of_experiment
with open('journal.txt', 'w') as f:
  print('+--------------------------------------------------+\n| Электронный лабораторный журнал                  |\n+--------------------------------------------------+', file=f)
  print(c1+ ' '*(51-len(c1))+ '|', sep='', file=f)
  print(c2+ ' '*(51-len(c2))+ '|', sep='', file=f)                    
  print(c3+ ' '*(51-len(c3))+ '|', sep='', file=f)
  print('+--------------------------------------------------+', file=f)
  print('| Вывод:' + 43*' ', '|', sep='', file=f)

  conclusion = conclusion.split()
  while len(conclusion) >= 4:
      line = ' '.join(conclusion[:5])
      print(f'| {line}' + (49-len(line))*' ' + '|', file=f)
      conclusion = conclusion[5:]
  print(f'| {' '.join(conclusion)}' + (49-len(conclusion[0]))*' ' + '|', file=f)
  print('+--------------------------------------------------+', file=f)
  # не получается на общий вывод делать красивую табличку, если слова длинные. сделала по примеру вывода. возможно. просто надо сделать таблицу шире, чтобы слова влезали
