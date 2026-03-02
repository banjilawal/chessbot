# src/command/pipeline/database/core/exception/push/duplicate.py

"""
Module: command.pipeline.database.core.exception.push.duplicate
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from logic.pipeline import PipelineStackException

__all__ = [
    # ======================# ADDING_DUPLICATE_PIPELINE EXCEPTION #======================#
    "AddingDuplicatePipelineException",
]


# ======================# ADDING_DUPLICATE_PIPELINE EXCEPTION #======================#
class AddingDuplicatePipelineException(PipelineStackException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to add a pipeline to teh stack failed because it was already present.

    # PARENT:
        *   PipelineStackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ADDING_DUPLICATE_PIPELINE_EXCEPTION"
    MSG = "Pushing pipeline onto stack failed: The pipeline is already present."