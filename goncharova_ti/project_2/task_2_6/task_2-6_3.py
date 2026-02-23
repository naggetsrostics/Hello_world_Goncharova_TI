donor = input("Введите фенотип группы крови донора (I, II, III, IV): ").strip().upper()
recepient = input("Введите фенотип группы крови рецепиента (I, II, III, IV): ").strip().upper()
if recepient == "I" and donor == 'I' :
    print("Переливание возможно")
elif (recepient == "II" and donor == 'I') or (recepient == 'II'  and donor == 'II'):
    print("Переливание возможно")
elif (recepient == "III" and donor == 'I') or (recepient == 'III'  and donor == 'III'):
    print("Переливание возможно")
elif (recepient == "IV" and donor == 'I') or (recepient == 'IV'  and donor == 'IV'):
    print("Переливание возможно")
else:
    print("Переливание крови не рекомендуется")
