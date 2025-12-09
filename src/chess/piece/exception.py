# src/chess/piece/exception.py

"""
Module: chess.piece.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    "PieceException",
    
#======================# PIECE NULL EXCEPTIONS #======================#

    
#======================# PIECE VALIDATION EXCEPTIONS #======================#
    "ActivePieceMissingFromTeamRoster",
    "CapturedPieceException",
    "PieceRequiresInitialPlacementException",

#======================# PIECE BUILD EXCEPTIONS #======================#

]


class PieceException(ChessException):
    """
    Super class of exceptions raised by Piece objects. Do not use directly. Subclasses give
    precise, fined-grained, debugging info.
    """
    ERROR_CODE = "PIECE_ERROR"
    DEFAULT_MESSAGE = "Piece raised an exception."


class ActivePieceMissingFromTeamRoster(PieceException):
    """Raised if an disabled Piece.team is set but Team.roster does not contain the Piece."""
    ERROR_CODE = "ACTIVE_PIECE_MISSING_FROM_TEAM_ROSTER_ERROR"
    DEFAULT_MESSAGE = (
        "Piece on the board, with Piece.team attribute set is not on it's team's roster."
    )











