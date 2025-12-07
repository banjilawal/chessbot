# src/chess/system/err/inconsistency.py

"""
Module: chess.system.err.inconsistency
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from chess.system.err import ChessException


__all__ = [
    # ======================# INCONSISTENCY EXCEPTION SUPER CLASS #======================#
    "InconsistencyException",
    # ======================# INCONSISTENT COLLECTION EXCEPTION #======================#
    "InconsistentCollectionException",
    # ======================# INVARIANT_BREACH EXCEPTION #======================#
    "InvariantBreachException",
]



# ======================# INCONSISTENCY EXCEPTION SUPER CLASS #======================#
class InconsistencyException(ChessException):
    """
    Raised if entity_service inconsistency is detected
    """
    ERROR_CODE = "DATA_INCONSISTENCY_ERROR"
    DEFAULT_MESSAGE = "A entity_service inconsistency was detected."


# ======================# INCONSISTENT COLLECTION EXCEPTION #======================#
class InconsistentCollectionException(InconsistencyException):
    """
    Raised if a data_set's state is inconsistent or its entity_service corrupted
    """
    ERROR_CODE = "INCONSISTENT_COLLECTION_ERROR"
    DEFAULT_MESSAGE = "Collection is an inconsistent state. Data might be corrupted."


# ======================# INVARIANT_BREACH EXCEPTION #======================#
class InvariantBreachException(ChessException):
    """
    Raised when a fundamental invariant of the system or environment is violated.
    This rollback_exception type signals a breach of consistency — meaning the system’s
    assumptions about its internal state are no longer valid.
    """
    DEFAULT_CODE = "INVARIANT_BREACH_ERROR"
    DEFAULT_MESSAGE = "A system invariant was violated, indicating a critical state inconsistency. or entity_service loss."
