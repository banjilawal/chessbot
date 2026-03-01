# src/chess/pipeline/database/core/exception/pop/unfound.py

"""
Module: chess.pipeline.database.core.exception.pop.unfound
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""


__all__ = [
    # ======================# PIPELINE_DOES_NOT_EXIST_FOR_REMOVAL EXCEPTION #======================#
    "PipelineDoesNotExistForRemovalException",
]

from chess.system import NullException
from chess.pipeline import PipelineStackException


# ======================# PIPELINE_DOES_NOT_EXIST_FOR_REMOVAL EXCEPTION #======================#
class PipelineDoesNotExistForRemovalException(PipelineStackException, NullException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to remove instances of a pipeline by a unique attribute failed because no bag
        matching the property were found in the dataset.

    # PARENT:
        *   PipelineDaaServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "PIPELINE_DOES_NOT_EXIST_FOR_REMOVAL_EXCEPTION"
    MSG = "Pipeline pop failed: The pipeline was not found in the dataset. Nothing to remove."