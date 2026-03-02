import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    df = person[person.duplicated(subset=['email'])]

    return df[['email']].drop_duplicates()
    