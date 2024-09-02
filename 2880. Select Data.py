import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    s = students['student_id'] == 101
    return students[s][['name','age']]