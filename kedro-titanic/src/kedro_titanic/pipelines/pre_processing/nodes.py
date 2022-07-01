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

def filter_dataset(df: pd.DataFrame):
    """This Function Filter Columns"""
    df = df[['Pclass', 'Sex', 'Age', 'SibSp', 
             'Parch', 'Fare', 'Embarked', 
             'Region_Cabin', 'Title', 'Survived']]

    return df

def encoding_dataset(df: pd.DataFrame):
    """This Function Encode Columns"""
    df = pd.get_dummies(df, 's_', columns=['Sex'], drop_first=True)
    df = pd.get_dummies(df, 't_', columns=['Title'], drop_first=True)
    df = pd.get_dummies(df, 'r_', columns=['Region_Cabin'], drop_first=True)
    df = pd.get_dummies(df, 'e_', columns=['Embarked'], drop_first=True)

    return df