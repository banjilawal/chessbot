# src/chess/square/collision.py

"""
Module: chess.square.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.piece import PieceException
from chess.system import (
    ChessException, NullException, ValidationException, BuildFailedException, InconsistencyException
)

__all__ = [
    "SquareException",
]


class SquareException(ChessException):
    """
    Super class of exceptions raised by Square objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "SQUARE_ERROR"
    DEFAULT_MESSAGE = "Square raised an exception."


# # ======================# RELATIONAL SQUARE EXCEPTIONS #======================#
# class InvalidPieceSquareRelationException(SquareException, PieceException, InconsistencyException):
#     """Catchall Exception for when SquareValidator fails candidates on a Piece-Square relationship test."""
#     ERROR_CODE = "PIECE_RELATES_TO_SQUARE_ERROR"
#     DEFAULT_MESSAGE = "Validation of Piece-Square relationship failed."
#
# class SquareAndPieceMismatchedCoordException(SquareException, PieceException):
#     """Raised if a Piece needs to occupy a Square before they are used together."""
#     ERROR_CODE = "SQUARE_AND_PIECE_COORD_MISMATCH_ERROR"
#     DEFAULT_MESSAGE = "Square and Piece do not share a target. They do not have a relationship."
#
#
# class PieceInconsistentSquareOccupationException(SquareException, PieceException, InconsistencyException):
#     """Raised if a Piece with the same Coord as a Square is not set as the Square's occupant"""
#     ERROR_CODE = "PIECE_INCONSISTENT_SQUARE_OCCUPATION_ERROR"
#     DEFAULT_MESSAGE = (
#         "A Piece sharing a Coord with a Square is not marked as the Square's occupant. There may be "
#         "service or data inconsistency."
#     )


