import pandas as pd


def left_join_and_select(
    left: pd.DataFrame, right: pd.DataFrame, on: str, columns: list[str]
) -> pd.DataFrame:
    """
    Perform a left join on two DataFrames and select specific columns.

    Args:
        left: Left DataFrame
        right: Right DataFrame
        on: Column name to join on
        columns: List of columns to select from result

    Returns:
        DataFrame with selected columns after left join
    """
    return pd.merge(left, right, on=on, how="left")[columns]
