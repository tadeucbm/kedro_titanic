"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline
from kedro_titanic.pipelines import pre_processing as pp
from kedro_titanic.pipelines import data_science as ds


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """

    pre_processing_pipeline = pp.create_pipeline()
    data_science_pipeline = ds.create_pipeline()

    return {
        "pp": pre_processing_pipeline,
        'ds': data_science_pipeline,
        "__default__": pre_processing_pipeline
        }
