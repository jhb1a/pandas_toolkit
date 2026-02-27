import pandas as pd

employee_table = pd.DataFrame(
    {
        "id": [1, 2, 3, 4, 5],
        "name": ["Joe", "Jim", "Henry", "Sam", "Max"],
        "salary": [70000, 90000, 80000, 60000, 90000],
        "departmentId": [1, 1, 2, 2, 1],
    },
)

department_table = pd.DataFrame({"id": [1, 2], "name": ["IT", "Sales"]})


def filter_by_group_agg(
    left_df: pd.DataFrame,
    right_df: pd.DataFrame,
    left_join_key: str,
    right_join_key: str,
    group_col: str,
    value_col: str,
    agg_func: str = "max",
    output_col_names: dict | None = None,
) -> pd.DataFrame:
    """
    Joins two DataFrames and returns rows where value_col matches
    an aggregated value within each group.

    Args:
        left_df:         Primary DataFrame.
        right_df:        Secondary DataFrame to join against.
        left_join_key:   Column in left_df to join on.
        right_join_key:  Column in right_df to join on.
        group_col:       Column (from right_df) to group by.
        value_col:       Column (from left_df) to aggregate and filter on.
        agg_func:        Aggregation — "max", "min", "mean", etc.
        output_col_names: Optional dict to rename output columns,
                          e.g. {"group_col": "Department", "value_col": "Salary"}.
    """
    merged_df = pd.merge(
        left_df,
        right_df,
        left_on=left_join_key,
        right_on=right_join_key,
        how="left",
        suffixes=("_left", "_right"),
    )

    # Resolve potential suffix collision on the group column
    if group_col in left_df.columns and group_col in right_df.columns:
        group_col = f"{group_col}_right"

    agg_values = merged_df.groupby(group_col)[value_col].agg(agg_func)
    result = pd.merge(merged_df, agg_values, on=[group_col, value_col])

    output_cols = [group_col, value_col] + [
        c for c in left_df.columns if c not in [left_join_key, value_col]
    ]
    result = result[[c for c in output_cols if c in result.columns]]

    if output_col_names:
        result = result.rename(columns=output_col_names)

    return result


print(
    filter_by_group_agg(
        employee_table,
        department_table,
        left_join_key="departmentId",
        right_join_key="id",
        group_col="name",
        value_col="salary",
        output_col_names={
            "name_right": "Department",
            "name_left": "Employee",
            "salary": "Salary",
        },
    )
)
