# src/command/pipeline/database/core/exception/pop/wrapper.py

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

from chess.pipeline import PipelineStackException
from chess.system import DeletionException


# ======================# POPPING_PIPELINE_STACK_FAILURE #======================#
class PoppingPipelineStackFailedException(PipelineStackException, DeletionException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why PipelineStack could not delete a pipeline. The exception chain traces the ultimate source of failure.

    # PARENT:
        *   PipelineStackException
        *   DeletionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "POPPING_PIPELINE_STACK_FAILURE"
    MSG = "Popping PipelineStack Failed."