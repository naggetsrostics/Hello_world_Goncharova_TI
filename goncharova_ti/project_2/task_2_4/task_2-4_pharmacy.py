total_capsules = int(input("Введите общее количество произведенных капсул: "))
in_one_package = int(input("Введите количество капсул в одной упаковке: "))

print('--- Отчет фасовочного цеха ---')
print(f'Полных упаковок:\t{total_capsules // in_one_package}\nОстаток капсул :\t{total_capsules % in_one_package}')
