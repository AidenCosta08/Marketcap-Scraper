import pandas as pd
marketcap_combined = pd.read_csv('marketcap_combined.csv')
def find_greatest():
    marketcap_combined['Rank'] = marketcap_combined['Rank'].str.replace('#', '').astype(int)
    max_rank=marketcap_combined['Rank'].max()
    return marketcap_combined['Rank']

def find_category(category):
    filtered_df = marketcap_combined[marketcap_combined['Categories'].str.contains(category)]
    matching_companies = filtered_df['Company'].tolist()
    return matching_companies


find_category("Recommerce")