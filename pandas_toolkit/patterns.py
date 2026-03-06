import pandas as pd


def find_consecutive_values(
    df: pd.DataFrame, column: str, consecutive_count: int
) -> pd.DataFrame:
    """
    Find values that appear consecutively N times in a column.

    Args:
        df: Input DataFrame
        column: Column name to check for consecutive values
        consecutive_count: Number of consecutive matches required

    Returns:
        DataFrame with one column containing unique consecutive values
    """
    df = df.copy()

    conditions = []
    for i in range(1, consecutive_count):
        conditions.append(df[column] == df[column].shift(-i))

    combined_condition = conditions[0]
    for condition in conditions[1:]:
        combined_condition = combined_condition & condition

    consecutive_rows: pd.DataFrame = df[combined_condition]
    result = consecutive_rows[column].drop_duplicates()

    return pd.DataFrame({"ConsecutiveValues": result})


def find_duplicates(
    df: pd.DataFrame, column: str, result_column_name: str = "Duplicates"
) -> pd.DataFrame:
    """
    Find duplicate values in a specified column.

    Args:
        df: Input DataFrame
        column: Column name to check for duplicates
        result_column_name: Name for the result column (default "Duplicates")

    Returns:
        DataFrame with one column containing unique duplicate values
    """
    duplicate_rows = df[df.duplicated(subset=column, keep=False)]
    result = duplicate_rows[column].drop_duplicates()

    return pd.DataFrame({result_column_name: result})


def delete_duplicates(
    df: pd.DataFrame, sort_by: str | list, columns: str | list
) -> pd.DataFrame:
    """
    Remove duplicate rows from a DataFrame based on specified columns.

    Args:
        df: Input DataFrame
        sort_by: Column name or list of column names to sort by before deduplication.
            Determines which row is kept when duplicates are found (lowest value wins).
        columns: Column name or list of column names that must all match for a row to be considered a duplicate.
            Multiple columns use AND logic - every specified column must match a previous row for it to be dropped.

    Returns:
        A new DataFrame with duplicates removed, sorted by sorty_by.

    """
    return df.sort_values(sort_by).drop_duplicates(subset=columns, keep="first")
