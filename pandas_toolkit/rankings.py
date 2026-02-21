from typing import Literal

import pandas as pd


def get_nth_highest(df: pd.DataFrame, column: str, n: int) -> pd.DataFrame:
    """
    Get the nth highest unique value from a specified column.

    Args:
        df: Input DataFrame
        column: Name of the column to find nth highest value from
        n: The rank to find (1 = highest, 2 = second highest, etc.)

    Returns:
        DataFrame with one row containing the nth highest value,
        or None if fewer than n unique values exist or n <= 0."""
    unique_df = df.drop_duplicates(subset=[column])
    sorted_df = unique_df.sort_values(by=[column], ascending=False)

    if len(sorted_df) < n or n <= 0:
        return pd.DataFrame({f"getNthHighest({n})": [None]})

    result = sorted_df[column].iloc[n - 1]

    return pd.DataFrame({f"getNthHighest({n})": [result]})


def rank_and_sort(
    df: pd.DataFrame,
    column: str,
    rank_method: Literal["dense", "min", "max", "average", "first"] = "dense",
) -> pd.DataFrame:
    """
    Rank values in a column and sort by that column descending.

    Args:
        df: Input DataFrame
        column: Column name to rank and sort by
        rank_method: Ranking method ('dense', 'min', 'max', 'average', 'first')

    Returns:
        DataFrame sorted by column with added 'rank' column"""
    df = df.copy()
    df["rank"] = df[column].rank(method=rank_method, ascending=False)

    return df.sort_values(by=[column], ascending=False)[[column, "rank"]]
