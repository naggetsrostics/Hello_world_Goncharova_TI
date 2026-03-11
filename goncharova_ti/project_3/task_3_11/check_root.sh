#!/bin/bash
check_root() {
   if [[ $EUID -eq 0 ]]; then
     echo "OK"
   else
     echo "Внимание! Скрипт запущен не от лица суперпользователя. Ошибка."
   fi
}

check_root
