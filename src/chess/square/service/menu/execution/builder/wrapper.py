# src/chess/square/service/menu/execution/builder/wrapper.py

"""
Module: chess.square.service.menu.execution.builder.wrapper
Author: Banji Lawal
Created: 2026-02-24
"""

from chess.square import BuildException

__all__ = [
    # ======================# SERVICE_EXECUTION_BUILD_FAILURE #======================#
    "ServiceExecutionBuildException",
]

# ======================# SERVICE_EXECUTION_BUILD_FAILURE #======================#
class ServiceExecutionBuildException(BuildException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in ServiceExecutionBuilder.build that, prevented BuildResult.success() from 
        being returned.

    # PARENT:
        *   BuildException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SERVICE_EXECUTION_BUILD_FAILED"
    DEFAULT_MESSAGE = "ServiceExecution build failed."