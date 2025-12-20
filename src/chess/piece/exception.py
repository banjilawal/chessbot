# src/chess/piece/exception.py

"""
Module: chess.piece.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    
#======================# PIECE VALIDATION EXCEPTION #======================#
    "ActivePieceMissingFromTeamRoster",

]

class ActivePieceMissingFromTeamRoster(PieceException):
    """Raised if an disabled Piece.team is set but Team.roster does not contain the Piece."""
    ERROR_CODE = "ACTIVE_PIECE_MISSING_FROM_TEAM_ROSTER_ERROR"
    DEFAULT_MESSAGE = (
        "Piece on the board, with Piece.team attribute set is not on it's team's roster."
    )











