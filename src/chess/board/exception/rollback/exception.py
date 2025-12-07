# src/chess/board/exception/rollback/base.py

"""
Module: chess.board.exception.rollback.exception
Author: Banji Lawal
Created: 2025-11-21
version: 1.0.0
"""


from chess.board import BoardException
from chess.system import RollbackException

__all__ = [
    "FailedPieceAdditionRolledBackException",
    "FailedPieceRemovalRolledBackException"
]

class FailedPieceAdditionRolledBackException(BoardException, RollbackException):
    """Raised after a Transaction rolled back changes when it could not add a Piece to a Board."""
    ERROR_CODE = "BOARD_PIECE_ADDITION_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "Adding the Piece to the Board failed during the Transaction. The transaction was rolled back "
        "before raising this exception."
    )


class FailedPieceRemovalRolledBackException(BoardException, RollbackException):
    """Raised after a Transaction rolled back changes when it could not remove a Piece to a Board."""
    ERROR_CODE = "BOARD_PIECE_REMOVAL_ERROR_ROLLED_BACK"
    DEFAULT_MESSAGE = (
        "Removing the Piece to the Board failed during the Transaction. The transaction was rolled back "
        "before raising this exception."
    )