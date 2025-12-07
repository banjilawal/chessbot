# src/chess/piece/service/data/__init__.py

"""
Module: chess.piece.entity_service.data.__init__
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.system import DataServiceException

__all__ = [
    "PieceDataServiceException",
]

class PieceDataServiceException(DataServiceException):
    ERROR_CODE = "PIECE_DATA_SERVICE_ERROR"
    DEFAULT_MESSAGE = "PieceDataService raised an exception."