# src/chess/domain/origin/exception.py

"""
Module: chess.domain.origin.exception
Author: Banji Lawal
Created: 2025-11-11
version: 1.0.0
"""

from chess.system import (
    ChessException, NullException, ValidationException, BuildFailedException, InconsistencyException
)

__all__ = [
    "DomainOriginException",
    
    # ====================== DOMAIN_ORIGIN GENERAL VALIDATION EXCEPTIONS #======================#
    "NullDomainOriginException",
    "InvalidDomainOriginException",
    
    # ====================== DOMAIN_ORIGIN VALIDATION EXCEPTIONS #======================#
    "CapturedPieceCannotActException",
    "PieceNotOnRosterCannotActException",
    "PieceNotOnBoardCannotActException",
    "CheckmatedKingCannotActException",
    
    # ====================== DOMAIN_ORIGIN BUILD EXCEPTIONS #======================#
    "DomainOriginBuildFailedException",
    
    # ====================== DOMAIN_ORIGIN SQUARE CONSISTENCY EXCEPTIONS #======================#
    "DomainOriginSquareNotFoundException",
    "PieceDoesNotOwnCurrentSquareException",
    "ActorAndScenePropCoordMismatchException",
]


class DomainOriginException(ChessException):
    ERROR_CODE = "DOMAIN_ORIGIN_ERROR"
    DEFAULT_MESSAGE = "An rollback_exception was raised by a DomainOrigin."


# ====================== DOMAIN_ORIGIN GENERAL VALIDATION EXCEPTIONS #======================#
class NullDomainOriginException(DomainOriginException, NullException):
    """"""
    ERROR_CODE = "NULL_DOMAIN_ORIGIN_ERROR"
    DEFAULT_MESSAGE = "A DomainOrigin cannot be null."


class InvalidDomainOriginException(DomainOriginException, ValidationException):
    """"""
    ERROR_CODE = "DOMAIN_ORIGIN_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "DomainOrigin validation failed."


# ====================== DOMAIN_ORIGIN VALIDATION EXCEPTIONS #======================#
class CapturedPieceCannotActException(DomainOriginException):
    """"""
    ERROR_CODE = "CAPTURED_PIECE_CANNOT_ACT_ERROR"
    DEFAULT_MESSAGE = "A captured piece cannot act in a scene."





class PieceNotOnRosterCannotActException(DomainOriginException):
    """"""
    ERROR_CODE = "PIECE_NOT_ON_ROSTER_CANNOT_ACT_ERROR"
    DEFAULT_MESSAGE = "A Piece must be on its Team roster to act in a scene"


class PieceNotOnBoardCannotActException(DomainOriginException):
    """"""
    ERROR_CODE = "PIECE_NOT_ON_BOARD_CANNOT_ACT_ERROR"
    DEFAULT_MESSAGE = "A piece must be on the board to act in a scene,"


class CheckmatedKingCannotActException(DomainOriginException):
    """"""
    ERROR_CODE = "CHECK_MATED_KING_CANNOT_ACT_ERROR"
    DEFAULT_MESSAGE = "A checkmated king cannot act in a scene."


# ====================== DOMAIN_ORIGIN BUILD EXCEPTIONS #======================#
class DomainOriginBuildFailedException(DomainOriginException, BuildFailedException):
    """"""
    ERROR_CODE = "DOMAIN_ORIGIN_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "DomainOrigin build failed."


# ====================== DOMAIN_ORIGIN SQUARE CONSISTENCY EXCEPTIONS #======================#
class DomainOriginSquareNotFoundException(DomainOriginException, InconsistencyException):
    """"""
    ERROR_CODE = "DOMAIN_ORIGIN_SQUARE_NOT_FOUND_ERROR"
    DEFAULT_MESSAGE = (
        "BoardSearch did not find a square associated with the actor_candidate's point. There may be a service "
        "inconsistency."
    )


class PieceDoesNotOwnCurrentSquareException(DomainOriginException, InconsistencyException):
    """"""
    ERROR_CODE = "PIECE_DOES_NOT_OWN_CURRENT_SQUARE_ERROR"
    DEFAULT_MESSAGE = (
        "The Piece sharing the Square's Coord is not marked as the Square occupant. "
        "There may be a service inconsistency."
    )



