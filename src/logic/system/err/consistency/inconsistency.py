# src/logic/system/err/inconsistency.py

"""
Module: logic.system.err.inconsistency
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from logic.system.err import ChessException


__all__ = [
    #======================# INCONSISTENCY EXCEPTION #======================#
    "InconsistencyException",
]



#======================# INCONSISTENCY EXCEPTION #======================#
class InconsistencyException(ChessException):
    """
    Raised if entity_service inconsistency is detected
    """
    ERR_CODE = "DATA_INCONSISTENCY_EXCEPTION"
    MSG = "A entity_service inconsistency was detected."

