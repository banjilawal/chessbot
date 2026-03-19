# src/command/pipeline/database/core/exception/pop/worker.py

"""
Module: command.pipeline.database.core.exception.pop.wrapper
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

__all__ = [
    # ======================# POPPING_PIPELINE_STACK_FAILURE #======================#
    "PoppingPipelineStackFailedException",
]

from logic.pipeline import PipelineStackException
from logic.system import DeletionException


# ======================# POPPING_PIPELINE_STACK_FAILURE #======================#
class PoppingPipelineStackFailedException(PipelineStackException, DeletionException):
    """
    Role:Exception Wrapper

    Responsibilities:
    1.  Wrap debug exceptions indicating why PipelineStack could not delete a pipeline. The exception chain traces the ultimate source of failure.

    Super Class:
        *   PipelineStackException
        *   DeletionException

    Provides:


    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "POPPING_PIPELINE_STACK_FAILURE"
    MSG = "Popping PipelineStack Failed."