import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['first'] = employees['name'].astype(str).str[0]

    employees['odd'] = employees['employee_id']%2 == 0

    for i in range(employees.shape[0]):
        if employees.loc[i,'first'] != 'M' and employees.loc[i,'odd'] == False:
            employees.loc[i, 'bonus'] = employees.loc[i, 'salary']
        else:
            employees.loc[i, 'bonus'] = 0

    employees = employees.sort_values(by='employee_id')
    return employees[['employee_id', 'bonus']]