proteins = int(input('Масса белков в продукте (г): '))
fat = int(input('Масса жиров в продукте (г): '))
carbohydrates = int(input('Масса углеводов в продукте (г): '))
calories = proteins*4 + fat*9 + carbohydrates*4
print(f'В продукте {calories} калорий')
