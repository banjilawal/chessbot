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
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that an attempt to add a pipeline to teh stack failed because it was already present.

    Super Class:
        *   PipelineStackException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ADDING_DUPLICATE_PIPELINE_EXCEPTION"
    MSG = "Pushing pipeline onto stack failed: The pipeline is already present."