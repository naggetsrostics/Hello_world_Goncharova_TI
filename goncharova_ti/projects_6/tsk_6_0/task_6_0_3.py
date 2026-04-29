import pandas as pd
with open("C:/Users/tanya/OneDrive/Desktop/task_6/medians.txt", "w", encoding='utf-8') as f:
    df = pd.read_csv("C:/Users/tanya/Downloads/wild_boars.csv")
    names = list(df.columns)
    for i in names[2:]:
        median =  df[i].median()
        l = i.split('_')
        if len(l) == 2:
            param = l[0] 
        else:
            param = l[0] + ' ' + l[1]
        print(f'Boars median {param} is {median:.2f} {l[-1]}\n', file=f)