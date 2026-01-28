import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()
    users_sorted = users.sort_values(by='user_id')
    return users_sorted