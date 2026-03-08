import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.groupby('activity_date')['user_id'].nunique().reset_index()
    activity = activity[activity.activity_date.between("2019-06-28","2019-07-27")]

    return activity.rename(columns = {'activity_date' : 'day', 'user_id' : 'active_users'})