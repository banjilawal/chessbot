# src/command/pipeline/database/core/exception/query/exist.py

"""
Module: command.pipeline.database.core.exception.query.exist
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""



__all__ = [
    # ======================# PIPELINE_NOT_FOUND EXCEPTION #======================#
    "PipelineNotFoundException",
]

from logic.pipeline import PipelineDebugException


# ======================# PIPELINE_NOT_FOUND EXCEPTION #======================#
class PipelineNotFoundException(PipelineDebugException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that an attempt to remove instances of a item by a unique attribute failed because no bag
        matching the property were found in the dataset.

    Super Class:
        *   NullException
        *   PipelineStackException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "PIPELINE_NOT_FOUND_EXCEPTION"
    MSG = "Pipeline deletion failed: The item was not found in the dataset. Nothing to remove."