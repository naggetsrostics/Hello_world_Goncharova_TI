print('=== Анализ последовательности ДНК ===')
nucleo = input('Введите последовательность ДНК: ')
print('Последовательность в верхнем регистре:', nucleo.upper())
print(f'Подсчёт нуклеотидов:\nA: {nucleo.count('A')}\nT: {nucleo.count('T')}\nG: {nucleo.count('G')}\nC: {nucleo.count('C')}\n\nОбщая длина: {len(nucleo)} нуклеотидов')
