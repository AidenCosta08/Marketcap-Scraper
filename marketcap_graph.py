import pandas as pd
import matplotlib.pyplot as plt

marketcap_combined = pd.read_csv('marketcap_combined.csv')
two_columns = marketcap_combined[['MarketCap', 'Country']]

map_dict = {
   "T": 10**9,
   "B": 10**6,
   "M": 10**3,
}

def convert_to_float(value):
   value = value.strip('$').split()
   return round(float(value[0]) * map_dict.get(value[1], 1))

t_df = two_columns[two_columns['MarketCap'].notna()]
t_df['MarketCap'] = t_df['MarketCap'].apply(convert_to_float)

grouped_data = t_df.groupby('Country')['MarketCap'].sum().nlargest(10)
grouped_data = grouped_data[1:]
grouped_data.plot.bar()

plt.xlabel('Country')
plt.ylabel('Total Market Cap')
plt.title('Total Market Cap by Country')

plt.show()
