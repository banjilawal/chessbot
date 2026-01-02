# src/chess/token/exception.py

"""
Module: chess.token.exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0
"""


__all__ = [
    
#======================# PIECE VALIDATION EXCEPTION #======================#
    "ActivePieceMissingFromTeamRoster",

]

class ActivePieceMissingFromTeamRoster(PieceException):
    """Raised if an disabled Token.team is set but Team.roster does not contain the Token."""
    ERROR_CODE = "ACTIVE_PIECE_MISSING_FROM_TEAM_ROSTER_ERROR"
    DEFAULT_MESSAGE = (
        "Token on the board, with Token.team attribute set is not on it's team's roster."
    )











