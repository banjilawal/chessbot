# src/chess/coord/builder/wrapper.py

"""
Module: chess.coord.builder.wrapper
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import BuildException

__all__ = [
    # ======================# COORD_BUILD_FAILURE #======================#
    "CoordBuildException",
]


# ======================# COORD_BUILD_FAILURE #======================#
class CoordBuildException(BuildException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in CoordBuilder.build that, prevented BuildResult.success() from
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
    ERR_CODE = "COORD_BUILD_FAILED"
    MSG = "Coord build failed."