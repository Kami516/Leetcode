import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    my_numbers = my_numbers.drop_duplicates(keep=False)
    numbers = my_numbers.sort_values(by='num', ascending=False)

    if len(numbers) > 0:
        return numbers.head(1)
    else:
        return pd.DataFrame({'num': [np.NaN]})
    