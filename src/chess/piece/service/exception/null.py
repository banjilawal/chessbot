# src/chess/piece/service//exception/null.py

"""
Module: chess.piece.service..exception.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import NullException
from chess.piece import InvalidPieceServiceException


__all__ = [
    "NullPieceServiceException",
]


#======================# NULL PIECE_SERVICE EXCEPTION #======================#
class NullPieceServiceException(InvalidPieceServiceException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate if an entity, method or operation required an PieceService but got null instead.

    # PARENT:
        *   InvalidPieceServiceException
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_PIECE_SERVICE_ERROR"
    DEFAULT_MESSAGE = "PieceService cannot be null."
