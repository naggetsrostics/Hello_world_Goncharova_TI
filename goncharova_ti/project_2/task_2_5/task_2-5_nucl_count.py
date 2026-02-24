print('=== Анализ последовательности ДНК ===')
print('Введите последовательность ДНК: ', end='')
with open("C:/Users/tanya/OneDrive/Desktop/Гончарова.txt", 'r', encoding='utf-8') as f:
  nucleo = f.read()
  print(nucleo)
  print('Последовательность в верхнем регистре:', nucleo.upper())
  print(f'Подсчёт нуклеотидов:\nA: {nucleo.count('A')}\nT: {nucleo.count('T')}\nG: {nucleo.count('G')}\nC: {nucleo.count('C')}\n\nОбщая длина: {len(nucleo)} нуклеотидов')
