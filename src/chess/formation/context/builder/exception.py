# src/chess/battleOrder/context/builder/exception.py

"""
Module: chess.battleOrder.context.builder.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import BuildFailedException
from chess.formation import BattleOrderContextException


__all__ = [
    #======================# TEAM_SCHEMA_CONTEXT BUILD EXCEPTIONS #======================#
    "BattleOrderContextBuildFailedException",
]


#======================# TEAM_SCHEMA_CONTEXT BUILD EXCEPTIONS #======================#
class BattleOrderContextBuildFailedException(BattleOrderContextException, BuildFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during BattleOrderContext build process.
    2.  Wraps unhandled exceptions that hit the try-finally block of an BattleOrderContextBuilder method.
    
    # PARENT:
        *   BattleOrderContextException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_SCHEMA_CONTEXT_BUILD_ERROR"
    DEFAULT_MESSAGE = "BattleOrderContext build failed."