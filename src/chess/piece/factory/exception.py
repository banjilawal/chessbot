# src/chess/piece/factory/exception

"""
Module: chess.piece.factoryory.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""


from chess.piece import PieceException
from chess.system import BuilderException


class PieceBuildFailedException(PieceException, BuilderException):
    """Catchall Exception for ScalarBuilder when it encounters an error building a Scalar."""
    ERROR_CODE = "PIECE_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Piece build failed."