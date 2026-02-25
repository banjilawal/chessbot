# src/chess/square/service/menu/operation/builder/wrapper.py

"""
Module: chess.square.service.menu.operation.builder.wrapper
Author: Banji Lawal
Created: 2026-02-24
"""

from chess.square import BuildException

__all__ = [
    # ======================# SERVICE_OPERATION_BUILD_FAILURE #======================#
    "ServiceOperationBuildException",
]

# ======================# SERVICE_OPERATION_BUILD_FAILURE #======================#
class ServiceOperationBuildException(BuildException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in ServiceOperationBuilder.build that, prevented BuildResult.success() from 
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
    ERROR_CODE = "SERVICE_OPERATION_BUILD_FAILED"
    DEFAULT_MESSAGE = "ServiceOperation build failed."