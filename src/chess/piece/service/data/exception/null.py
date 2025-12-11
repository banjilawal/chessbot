# src/chess/piece/service/data/exception/null.py

"""
Module: chess.piece.service.data.exception.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import NullException
from chess.piece import InvalidPieceDataServiceException


__all__ = [
    "NullPieceDataServiceException",
    "PieceNullDataSetException",
]


#======================# NULL PIECE_DATA_SERVICE EXCEPTION #======================#
class NullPieceDataServiceException(InvalidPieceDataServiceException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate if an entity, method or operation required an PieceDataService but got null instead.

    # PARENT:
        *   InvalidPieceDataServiceException
        *   NullException

    # PROVIDES:
    Nnone

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_PIECE_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "PieceDataService cannot be null."


#======================# PIECE_NULL_DATA_SET EXCEPTION #======================#
class PieceNullDataSetException(InvalidPieceDataServiceException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that PieceDataService.items does not exist.

    # PARENT:
        *   InvalidPieceDataServiceException
        *   NullException

    # PROVIDES:
    PieceNullDataSetException

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "PIECE_NULL_DATA_SET_ERROR"
    DEFAULT_MESSAGE = "PieceDataService cannot have a null list of items."