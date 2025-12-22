# src/chess/formation/builder/exception.py

"""
Module: chess.formation.builder.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import BuildFailedException
from chess.formation import OrderContextException

__all__ = [
    # ======================# TEAM_SCHEMA_SUPER_KEY BUILD EXCEPTION #======================#
    "OrderContextBuildFailedException",
]


# ======================# TEAM_SCHEMA_SUPER_KEY BUILD EXCEPTION #======================#
class OrderContextBuildFailedException(OrderContextException, BuildFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during OrderContext build process.
    2.  Wrap an exception that hits the try-finally block of an OrderContextBuilder method.

    # PARENT:
        *   FormationSuperKeyException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_SCHEMA_SUPER_KEY_BUILD_ERROR"
    DEFAULT_MESSAGE = "OrderContext build failed."