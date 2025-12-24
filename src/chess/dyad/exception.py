# src/chess/dyad/exception.py

"""
Module: chess.dyad.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system.err import ChessException

__all__ = [
    # ======================# SCHEMAAGENTPAIR EXCEPTION #======================#
    "SchemaAgentPairException",
]


# ======================# SCHEMAAGENTPAIR EXCEPTION #======================#
class SchemaAgentPairException(ChessException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for SchemaAgentPair errors not covered by SchemaAgentPairException subclasses.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "SCHEMAAGENTPAIR_ERROR"
    DEFAULT_MESSAGE = "SchemaAgentPair raised an exception."