weight = float(input("Введите ваш вес (кг): "))
height = float(input("Введите ваш рост (м): "))

bmi = weight / (height ** 2)
print('--- Отчет о состоянии здоровья ---')
print(f'Рост:\t{height}\nВес :\t{weight}\nИндекс массы тела: {bmi:.2f}')
