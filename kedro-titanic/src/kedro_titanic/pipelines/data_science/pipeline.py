"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import split_data, fit_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = split_data,
            inputs = 'fe_train'
            output = ['X_train', 'X_test', 'y_train', 'y_test']
            name = 'split_data'
        ),
        node(
            func = split_data,
            inputs = ['X_train', 'X_test', 'y_train', 'y_test']
            output = ['classifier']
            name = 'fit_model'
        )
    ])
