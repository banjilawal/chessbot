# src/chess/system/resolution/exception/failure/square/exception.py

"""
Module: chess.system.resolution.exception.failure.square.exception
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""


from chess.system.resolution import ResolutionFailedException

_

__all__ = [
    "ResolvingCoordConflictFailedException",
    "ResolvingSquareCoordConflictFailedException",
    "ResolvingPieceCoordConflictFailedException",
]


class ResolvingCoordConflictFailedException(ResolutionFailedException):
    ERROR_CODE = "RESOLUTION_FAILED_ERROR"
    DEFAULT_MESSAGE = "The resolution process failed to break the attribute conflict."


class ResolvingSquareCoordConflictFailedException(ResolvingCoordConflictFailedException):
    """Each square_name has a fixed unique square_name. Searching squares by their unique square_name attribute
     should return a single hit. Raise this exception if SquareResolver leaves orphan squares that
      cannot be linked ot a game or a board. returned multiple hits."""
    DEFAULT_CODE = "SQUARE_COORD_CONFLICT_RESOLUTION_ERROR"
    DEFAULT_MESSAGE = "The resolution process failed to break the Square.square_name conflict."


class ResolvingPieceCoordConflictFailedException(ResolvingCoordConflictFailedException):
    DEFAULT_CODE = "PIECE_COORD_CONFLICT_RESOLUTION_ERROR"
    DEFAULT_MESSAGE = "The resolution process failed to break the Token.square_name conflict."
