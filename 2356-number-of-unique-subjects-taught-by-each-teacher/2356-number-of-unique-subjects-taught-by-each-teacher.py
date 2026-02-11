import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    teacher = teacher.groupby('teacher_id')['subject_id'].nunique()
    teacher = teacher.reset_index()
    teacher = teacher.rename(columns={'subject_id':'cnt'})

    return teacher