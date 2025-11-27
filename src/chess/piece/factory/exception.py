# src/chess/piece/factory/exception

"""
Module: chess.piece.factory.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""


from chess.piece import PieceException
from chess.system import BuilderException, BuildFailedException, NullException

__all__ = [
    "PieceBuildFailedException",
    "NullPieceFactoryException",
]

class PieceBuildFailedException(PieceException, BuildFailedException):
    """
    Catchall exception for when PieceBuilder encounters an error building a new Piece instance.
    """
    ERROR_CODE = "PIECE_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Piece build failed."


class NullPieceFactoryException(BuilderException, NullException):
    """Raised when an entity, method, or operation requires a PieceFactory but gets null instead."""
    ERROR_CODE = "NULL_PIECE_FACTORY_ERROR"
    DEFAULT_MESSAGE = "PieceFactory cannot be null."