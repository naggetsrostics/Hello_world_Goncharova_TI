operator_name = input("Введите имя оператора: ")
current_pressure = input("Введите текущее значение давления (Па): ")
with open("sensor_log.txt", "w", encoding="utf-8") as f:
    f.write(f"{operator_name}\t{current_pressure}")
print("Данные успешно сохранены в 'sensor_log.txt'")
