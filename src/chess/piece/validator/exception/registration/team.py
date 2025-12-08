# src/chess/piece/validator/exception/registration/base.py

"""
Module: chess.piece.validator.exception.registration.base_
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.piece import InvalidPieceException
from chess.system import RegistrationException

__all__ = [
    # ======================# PIECE_NOT_REGISTERED_WITH_ROSTER EXCEPTION #======================#
    "PieceNotRegisteredWithTeamException"
]

# ======================# PIECE_NOT_REGISTERED_WITH_ROSTER EXCEPTION #======================#
class PieceNotRegisteredWithTeamException(PieceRegistrationException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that while the Piece has assigned itself to a Team but the piece is not included in the
        Team's roster.
    2.  That is piece.team = team but piece not in team.roster.

    # PARENT:
        *   PieceRegistrationException

    # PROVIDES:
    PieceNotRegisteredWithTeamException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PIECE_NOT_REGISTERED_WITH_TEAM_ERROR"
    DEFAULT_MESSAGE = (
        "Piece is not registered in Team.roster. Only the piece-side of the relationship is set."
    )