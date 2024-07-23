import pandas as pd

directory = '/Users/aiden/Downloads/Marketcap Scraper'

df_list = []

for i in range(1, 88 + 1):
    filename = f'marketcap{i}.csv'
    file_path = f'{directory}/{filename}'
    df = pd.read_csv(file_path)
    df_list.append(df)

combined_df = pd.concat(df_list, ignore_index=True)

combined_df.pop('Unnamed: 0') 
combined_df.to_csv(f'{directory}/marketcap_combined.csv', index=False)