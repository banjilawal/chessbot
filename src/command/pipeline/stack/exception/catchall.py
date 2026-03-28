# src/command/pipeline/database/kernel/exception/super.py

"""
Module: command.pipeline.database.kernel.exception.super
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

___all__ = [
    # ======================# PIPELINE_STACK_SERVICE EXCEPTION #======================#
    "PipelineStackException",
]

from logic.pipeline import PipelineException
from logic.system import StackServiceException


# ======================# PIPELINE_STACK_SERVICE EXCEPTION #======================#
class PipelineStackException(PipelineException, StackServiceException):
    """
    Role:Exception Wrapper

    Responsibilities:
    1.  Encapsulate PipelineStack method outputs when there is a failure.

    Super Class:
        *   PipelineException
        *   StackServiceException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "PIPELINE_STACK_SERVICE_EXCEPTION"
    MSG = "PipelineStack raised an exception."