# src/chess/piece/context/entity_service/base.py

"""
Module: chess.piece.context.entity_service.exception
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

from chess.system import ServiceException

__all__ = [
    # ======================# PIECE_CONTEXT_SERVICE EXCEPTIONS #======================#
    "PieceContextServiceException"
]


# ======================# PIECE_CONTEXT_SERVICE EXCEPTIONS #======================#
class PieceContextServiceException(ServiceException):
    """
    Super class of exceptions raised by PieceContextService objects.
    Do not use directly. Subclasses give precise, fined-grained, debugging info.
    """
    ERROR_CODE = "PIECE_CONTEXT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "PieceContextService raised an exception."