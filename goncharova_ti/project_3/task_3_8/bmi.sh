#!/bin/bash
read -r -p "Введите ваш вес (в кг): " WEIGHT
read -r -p "Введите ваш рост (в м): " HEIGHT

# Вычисление с использованием bc для дробных чисел
BMI=$(echo "scale=0; $WEIGHT / ($HEIGHT * $HEIGHT)" | bc -l)

# Вывод с интерполяцией
echo "Ваш примерный ИМТ: $BMI"
