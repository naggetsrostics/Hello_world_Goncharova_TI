import pandas as pd
with open("C:/Users/tanya/OneDrive/Desktop/task_6/percentiles_lenght.txt", "w", encoding='utf-8') as f:
    df = pd.read_csv("C:/Users/tanya/Downloads/wild_boars.csv")
    q1 = df.groupby('gender')['length_cm'].quantile(0.25)
    q3 = df.groupby('gender')['length_cm'].quantile(0.75)
    print("IQR:", file=f)
    print(q3-q1, file=f)
