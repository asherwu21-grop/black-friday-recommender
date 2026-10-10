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

t = t.reset_index() # Makes product_id and product_name appear, they aren't indexes anymore

# Format the dataframe as a Markdown table, using tabulate
markdown_table = t.to_markdown(index=False)

# Now write:
t.to_csv('safe_range.csv', index = False)

with open('RESULTS.md', 'w') as f:
    f.write("8 was chosen as the cutoff as it is reasonably long to judge a season sales.\n\n")
    f.write(markdown_table)
    f.write("\n")
