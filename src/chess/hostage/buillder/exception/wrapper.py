# src/chess/hostage/builder/exception.py

"""
Module: chess.hostage.builder.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


__all__ = [
    # ======================# Hostage_BUILD_FAILURE #======================#
    "HostageBuildException",
]

from chess.system import BuildException

# ======================# Hostage_BUILD_FAILURE #======================#
class HostageBuildException(BuildException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in HostageBuilder.build that, prevented BuildResult.success() from
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
    ERR_CODE = "Hostage_BUILD_FAILED"
    MSG = "Hostage build failed."