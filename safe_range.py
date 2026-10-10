import pandas as pd

df = pd.read_csv('data/weekly_sales.csv')

# Group data by product and calculate statistics

t = df.groupby(['product_id', 'product_name']).agg(
        weeks=('week_start_date', 'nunique'), # Count #unique weeks
        low=('price', 'min'), # Lowest seen price
        high=('price','max'), # Highest seen price
        prices=('price', 'nunique') # Unique Prices
    )
t['single_price'], t['sparse'] = t['prices'].apply(lambda v: v == 1), t['weeks'].apply(lambda n: n < 8)

t.to_csv('safe_range.csv', index = False)
# 
