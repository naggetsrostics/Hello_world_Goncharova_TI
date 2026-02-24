V = float(input("Необходимыйобъем раствора (мл): "))
M = round(V*0.009, 2)
with open('C:/Users/tanya/OneDrive/Desktop/recipe.txt', 'w', encoding='utf-8') as f:
  f.write(f'ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n-----------------------\nОбщий объем:\t{V} мл\nМасса соли:\t{M} г\nОбъем воды:\t{V} мл')
