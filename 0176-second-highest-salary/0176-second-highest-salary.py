import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    unique= employee['salary'].drop_duplicates()

    if len(unique)<2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    else:
        sorted_emp = unique.sort_values(ascending=False)
        highest = sorted_emp.iloc[1]
        return pd.DataFrame({'SecondHighestSalary': [highest]})