"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.1
"""

from sklearn import model_selection as ms
from sklearn import linear_model as lm
from sklearn import metrics as me

def split_data(df):
    X = df.drop('Survived', axis=1)
    y = df.loc[:, 'Survived']

    X_train, X_test, y_train, y_test = ms.train_test_split(X, y, test_size=0.2, random_state=32, stratify=y)

    return X_train, X_test, y_train, y_test


def fit_model():
    imp = SimpleImputer(missing_values=np.nan, strategy=imput_strat)
    model = lm.LogisticRegression(random_state=32)
    
    pipeline = Pipeline([
        ('imp', imp),
        ('clf', model)
        ])

    train_model = pipeline.fit(X_train, y_train)
    
    return train_model