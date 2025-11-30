# src/chess/board/validator/exception.py

"""
Module: chess.board.validator.exception
Author: Banji Lawal
Created: 2025-11-21
version: 1.0.0
"""


class InvalidBoardException(BoardException, ValidationException):
    """Catchall Exception for BoardValidator when a candidate fails a sanity check."""
    ERROR_CODE = "BOARD_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Board validation failed."


class NullBoardException(BoardException, NullException):
    """Raised if an entity, method, or operation requires Board but gets null instead."""
    ERROR_CODE = "NULL_BOARD_ERROR"
    DEFAULT_MESSAGE = "Board cannot be validation"


class BoardNullPieceListException(BoardException, NullException):
    """Raised if a Board.pieces list does not exist. This should never happen."""
    ERROR_CODE = "MISSING_PIECES_LIST_ERROR"
    DEFAULT_MESSAGE = "The Board.pieces list is validation. There may be a service failure or data inconsistency."


class BoardNullSquareListException(BoardException, NullException):
    """Raised if a Board.squares list does not exist. This should never happen."""
    ERROR_CODE = "BOARD_MISSING_SQUARE_LIST_ERROR"
    DEFAULT_MESSAGE = "The Board.squares list is validation. There may be a service failure or data inconsistency."