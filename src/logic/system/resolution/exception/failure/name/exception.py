# src/logic/system/resolution/exception/failure/designation/exception.py

"""
Module: logic.system.resolution.exception.failure.designation.exception
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""


from logic.system.resolution import ResolutionFailedException


__all__ = [
    "ResolvingNameConflictFailedException",
    "ResolvingSquareNameConflictFailedException",
    "ResolvingPieceNameConflictFailedException",
    "ResolvingAgentNameConflictFailedException"
]

class ResolvingNameConflictFailedException(ResolutionFailedException):
    ERR_CODE = "RESOLUTION_FAILED_EXCEPTION"
    MSG = "The resolution process failed to break the attribute conflict."


class ResolvingSquareNameConflictFailedException(ResolvingNameConflictFailedException):
    DEFAULT_CODE = "SQUARE_NAME_CONFLICT_RESOLUTION_EXCEPTION"
    MSG = "The resolution process failed to break the Square.designation conflict."


class ResolvingPieceNameConflictFailedException(ResolvingNameConflictFailedException):
    DEFAULT_CODE = "PIECE_NAME_CONFLICT_RESOLUTION_EXCEPTION"
    MSG = "The resolution process failed to break the Token.designation conflict."


class ResolvingAgentNameConflictFailedException(ResolvingNameConflictFailedException):
    DEFAULT_CODE = "AGENT_NAME_CONFLICT_RESOLUTION_EXCEPTION"
    MSG = "The resolution process failed to break the Player.designation conflict."