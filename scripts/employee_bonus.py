import pandas as pd

employee = pd.DataFrame(
    {
        "empId": [3, 1, 2, 4],
        "name": ["Brad", "John", "Dan", "Thomas"],
        "supervisor": [None, 3, 3, 3],
        "salary": [4000, 1000, 2000, 4000],
    }
)

bonus = pd.DataFrame({"empId": [2, 4], "bonus": [500, 2000]})


def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(employee, bonus, on="empId", how="left")
    df = df.loc[(df["bonus"] < 1000) | (df["bonus"].isna())]

    return df[["name", "bonus"]]


print(employee_bonus(employee, bonus))
