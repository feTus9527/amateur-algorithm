import pandas as pd


def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(sales, product, how="left", on="product_id").loc[
        :, ["product_name", "year", "price"]
    ]
