import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    employee['max_salary'] = employee.groupby('departmentId')['salary'].transform('max')
    highest_salaries = employee[employee['salary'] == employee['max_salary']]
    result = highest_salaries.merge(department, left_on='departmentId', right_on='id', suffixes=('_emp', '_dept'))
    return result[['name_dept', 'name_emp', 'salary']].rename(columns={
        'name_dept': 'Department',
        'name_emp': 'Employee',
        'salary': 'Salary'
    })

    return result