#!/bin/bash
read -r -p "Введите название гена: " GEN
read -r -p "Введите уровень экспрессии гена: " EXPRESSION

if [[ $# -lt 2 ]];  then
  echo "Ошибка! Нужно 2 аргумента"
  exit 1 
fi

echo "Экспрессия гена $GENE составляет $EXPRESSION единиц"

