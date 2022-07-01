"""
This is a boilerplate pipeline 'pre_processing'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import feature_engineering


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = feature_engineering,
            inputs = 'train',
            outputs = 'fe_train',
            name = 'df_featured'
        )
    ])
