import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities.groupby('sell_date')['product'].agg([
        ('num_sold', 'nunique'),
        ('products', lambda x: ','.join(sorted(x.unique())))])
    return activities.reset_index()