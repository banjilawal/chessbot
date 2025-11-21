# src/chess/piece/validator/exception/binding/collision.py
"""
Module: chess.piece.validator.exception.binding.exception
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""
from chess.piece import PieceException
from chess.system import (
    ChessException, BuilderException, InconsistencyException, NoBindingException, NullException, ValidationException
)

__all__ = [
    "PieceException",
    
    # ======================# PIECE NULL EXCEPTIONS #======================#
    "NullPieceException",
    "NullKingException",
    "NullCombatantException",
    "PieceTeamFieldIsNullException",
    "PieceNoCoordStackServiceException",
    "PieceNullCoordStackException",
    "PieceRosterNumberIsNullException",
    
    # ======================# PIECE VALIDATION EXCEPTIONS #======================#
    "InvalidPieceException",
    "ActivePieceMissingFromTeamRoster",
    "CheckmatedKingException",
    "CapturedPieceException",
    "PieceRequiresInitialPlacementException",
    
    "PieceRankOutOfBoundsException",
    "PieceMissingDiscoveriesException",

]

class PieceNotBoundException(PieceException, NoBindingException):
    ERROR_CODE = "PIECE_NOT_BOUND_ERROR"
    DEFAULT_MESSAGE = "Piece does not have a binding. The piece cannot act."
    
class TeamRosterNotBoundToPieceException(PieceNotBoundException):
    ERROR_CODE = "TEAM_ROSTER_NOT_BOUND_TO_PIECE_ERROR"
    DEFAULT_MESSAGE = "Piece does not have a binding to the team's roster. The piece cannot act."


class PieceNotBoundToSquareException(PieceNotBoundException):
    ERROR_CODE = "PIECE_NOT_BOUND_TO_SQUARE_ERROR"
    DEFAULT_MESSAGE = (
        "Piece does not have a binding to the Square. The Piece cannot act from a "
        "Square it does not ocupy."
    )


class PieceNotBoundToBoardException(PieceNotBoundException):
    ERROR_CODE = "PIECE_NOT_BOUND_TO_BOARD_ERROR"
    DEFAULT_MESSAGE = (
        "Piece does not have a binding to the Board. The Piece cannot act when it is not "
        "on the board."
    )