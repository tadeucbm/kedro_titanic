"""
This is a boilerplate pipeline 'pre_processing'
generated using Kedro 0.18.1
"""
import pandas as pd
import numpy as np

def feature_engineering(df: pd.DataFrame):
    """This Function Create new features"""
    # Region
    df['Region_Cabin'] = df['Cabin'].apply(lambda x: str(x)[0] if x is not np.nan else 'empty')

    # Title
    df['Title'] = df['Name'].apply(lambda x: str(x).split(',')[1].split('.')[0])

    return df