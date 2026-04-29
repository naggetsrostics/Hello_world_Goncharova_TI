import pandas as pd
with open("C:/Users/tanya/OneDrive/Desktop/task_6/variations_tusk_lenght.txt", "w", encoding='utf-8') as f:
    df = pd.read_csv("C:/Users/tanya/Downloads/wild_boars.csv")
    cv = (df.groupby('gender')['tusk_length_cm'].std() / df.groupby('gender')['tusk_length_cm'].mean()) * 100
    print(f'Coefficient of variations:\n{cv}', file=f)
