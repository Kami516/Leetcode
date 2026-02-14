import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:

    orders = orders.groupby('customer_number')['order_number'].nunique()
    orders = orders.reset_index()
    orders = orders.sort_values(by='order_number', ascending=False)
    del orders['order_number']

    return orders.head(1)