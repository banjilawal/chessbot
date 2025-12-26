# src/chess/system/err/inconsistency.py

"""
Module: chess.system.err.inconsistency
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from chess.system.err import ChessException


__all__ = [
    #======================# INCONSISTENCY EXCEPTION #======================#
    "InconsistencyException",
]



#======================# INCONSISTENCY EXCEPTION #======================#
class InconsistencyException(ChessException):
    """
    Raised if entity_service inconsistency is detected
    """
    ERROR_CODE = "DATA_INCONSISTENCY_ERROR"
    DEFAULT_MESSAGE = "A entity_service inconsistency was detected."

