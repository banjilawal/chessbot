# src/command/pipeline/database/core/exception/push/wrapper.py

"""
Module: command.pipeline.database.core.exception.push.wrapper
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# PIPELINE_PUSH_FAILURE #======================#
    "PushingPipelineFailedException",
]

from chess.pipeline import PipelineStackException
from chess.system import InsertionException


# ======================# PIPELINE_PUSH_FAILURE #======================#
class PushingPipelineFailedException(PipelineStackException, InsertionException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that pushing a Pipeline on the Stack failed.

    # PARENT:
        *   PipelineStackException
        *   InsertionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "PIPELINE_PUSH_FAILURE"
    MSG = "Pipeline push failed."