#!/bin/bash
CURRENT_YEAR=2026
echo "Enter a year"
read -r BIRTH_YEAR
echo $BIRTH_YEAR
# Вычисление (Арифметика)
AGE=$((CURRENT_YEAR - BIRTH_YEAR))

# Вывод с интерполяцией
echo "Текущий год: $CURRENT_YEAR"
echo "Ваш примерный возраст: $AGE"

