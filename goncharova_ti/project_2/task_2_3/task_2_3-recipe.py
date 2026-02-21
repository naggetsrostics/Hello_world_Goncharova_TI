nutrient_medium = input("Введите название питательной среды: ")
agar_concentration = input("Введите концентрацию агара (%): ")
sterilization_temperature = input("Введите температуру стерилизации ( °C): ")
with open("recipe.txt", "w", encoding="utf-8") as f:
    f.write(f"{nutrient_medium.upper()}\n")
    f.write(f"Концентрация агара:\t        {agar_concentration}\nТемпература стерилизации:\t{sterilization_temperature}")
print("Файл 'recipe.txt' успешно сформирован!")
