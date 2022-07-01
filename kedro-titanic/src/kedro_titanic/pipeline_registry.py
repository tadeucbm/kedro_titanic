"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline
from kedro_titanic.pipelines import pre_processing as pp


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """

    pre_processing_pipeline = pp.create_pipeline()

    return {
        "pp": pre_processing_pipeline,
        "__default__": pre_processing_pipeline
        }
