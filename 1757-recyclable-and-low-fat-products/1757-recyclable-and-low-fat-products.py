import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    sorted_products = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return sorted_products[['product_id']]