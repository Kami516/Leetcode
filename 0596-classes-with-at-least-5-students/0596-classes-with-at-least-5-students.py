import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    courses = courses.groupby('class')['student'].count()
    courses = courses.reset_index()
    result = courses[courses['student']>=5]
    del result['student']
    
    return result