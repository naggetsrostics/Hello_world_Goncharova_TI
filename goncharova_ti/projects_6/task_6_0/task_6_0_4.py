import pandas as pd
with open("C:/Users/tanya/OneDrive/Desktop/task_6/modes.txt", "w", encoding='utf-8') as f:
    df = pd.read_csv("C:/Users/tanya/Downloads/wild_boars.csv")
    names = list(df.columns)
    for i in names[1:]:
        mode =  df[i].mode()
        l = i.split('_')
        if len(l) == 2 or len(l) == 1:
            param = l[0] 
        else:
            param = l[0] + ' ' + l[1]
        print(f'Boars mode {param} is {mode[0]} {l[-1]}\n', file=f)