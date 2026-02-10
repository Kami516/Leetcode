import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    new_table = pd.melt(products, id_vars=['product_id'], value_vars=['store1','store2','store3'])

    new_table = new_table.dropna()
    new_table = new_table.rename(columns={'variable':'store', 'value':'price'})

    return new_table