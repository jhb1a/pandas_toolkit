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


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame):
    merged_df = pd.merge(
        employee, department, left_on="departmentId", right_on="id", how="left"
    ).rename(columns={"name_x": "Employee", "name_y": "Department", "salary": "Salary"})
    max_salaries = merged_df.groupby("Department")["Salary"].max()
    result = pd.merge(merged_df, max_salaries, on=["Department", "Salary"])

    return result[["Department", "Employee", "Salary"]]
