"""
This is a boilerplate pipeline 'pre_processing'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import feature_engineering, filter_dataset, encoding_dataset


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = feature_engineering,
            inputs = 'train',
            outputs = 'fe_train',
            name = 'df_featured'
        ),
        node(
            func = filter_dataset,
            inputs = 'fe_train',
            outputs = 'filtered_train',
            name = 'df_filtered'
        ),
        node(
            func = encoding_dataset,
            inputs = 'filtered_train',
            outputs = 'encoded_train',
            name = 'df_encoded'
        )
    ])
