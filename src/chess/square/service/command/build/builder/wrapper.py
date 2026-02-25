# src/chess/square/service/build/request/builder/wrapper.py

"""
Module: chess.square.service.build.request.builder.wrapper
Author: Banji Lawal
Created: 2026-02-24
"""

from chess.square import BuildException

__all__ = [
    # ======================# SERVICE_REQUEST_BUILD_FAILURE #======================#
    "ServiceRequestBuildException",
]

# ======================# SERVICE_REQUEST_BUILD_FAILURE #======================#
class ServiceRequestBuildException(BuildException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in ServiceRequestBuilder.build that, prevented BuildResult.success() from 
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
    ERR_CODE = "SERVICE_REQUEST_BUILD_FAILED"
    MSG = "ServiceRequest build failed."