# src/chess/system/resolution/exception/failure/designation/exception.py

"""
Module: chess.system.resolution.exception.failure.designation.exception
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""


from chess.system.resolution import ResolutionFailedException


__all__ = [
    "ResolvingNameConflictFailedException",
    "ResolvingSquareNameConflictFailedException",
    "ResolvingPieceNameConflictFailedException",
    "ResolvingAgentNameConflictFailedException"
]

class ResolvingNameConflictFailedException(ResolutionFailedException):
    ERROR_CODE = "RESOLUTION_FAILED_ERROR"
    DEFAULT_MESSAGE = "The resolution process failed to break the attribute conflict."


class ResolvingSquareNameConflictFailedException(ResolvingNameConflictFailedException):
    DEFAULT_CODE = "SQUARE_NAME_CONFLICT_RESOLUTION_ERROR"
    DEFAULT_MESSAGE = "The resolution process failed to break the Square.designation conflict."


class ResolvingPieceNameConflictFailedException(ResolvingNameConflictFailedException):
    DEFAULT_CODE = "PIECE_NAME_CONFLICT_RESOLUTION_ERROR"
    DEFAULT_MESSAGE = "The resolution process failed to break the Piece.designation conflict."


class ResolvingAgentNameConflictFailedException(ResolvingNameConflictFailedException):
    DEFAULT_CODE = "AGENT_NAME_CONFLICT_RESOLUTION_ERROR"
    DEFAULT_MESSAGE = "The resolution process failed to break the PlayerAgent.designation conflict."