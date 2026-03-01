# src/command/pipeline/database/core/exception/pop/empty

"""
Module: command.pipeline.database.core.exception.pop.empty
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""



__all__ = [
    # ======================# POPPING_EMPTY_PIPELINE_STACK EXCEPTION #======================#
    "PoppingEmptyPipelineStackException",
]

from chess.system import NullException
from chess.pipeline import PipelineStackException


# ======================# POPPING_EMPTY_PIPELINE_STACK EXCEPTION #======================#
class PoppingEmptyPipelineStackException(PipelineStackException, NullException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to remove a pipeline failed because the PipelineStack was not managing any pipelines.

    # PARENT:
        *   PipelineDaaServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "POPPING_EMPTY_PIPELINE_STACK_EXCEPTION"
    MSG = "Pipeline pop failed: The stack is empty. Nothing to delete"