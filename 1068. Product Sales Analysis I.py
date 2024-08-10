import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    table = pd.merge(sales, product, on="product_id")
    return table[['product_name', 'year', 'price']]