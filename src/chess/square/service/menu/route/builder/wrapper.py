# src/chess/square/service/menu/route/builder/wrapper.py

"""
Module: chess.square.service.menu.route.builder.wrapper
Author: Banji Lawal
Created: 2026-02-24
"""

from chess.square import BuildException

__all__ = [
    # ======================# SERVICE_ROUTE_BUILD_FAILURE #======================#
    "ServiceRouteBuildException",
]

# ======================# SERVICE_ROUTE_BUILD_FAILURE #======================#
class ServiceRouteBuildException(BuildException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in ServiceRouteBuilder.build that, prevented BuildResult.success() from 
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
    ERROR_CODE = "SERVICE_ROUTE_BUILD_FAILED"
    DEFAULT_MESSAGE = "ServiceRoute build failed."