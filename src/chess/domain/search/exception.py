# src/chess/points/searcher/exception

"""
Module: chess.points.searcher.exception
Author: Banji Lawal
Created: 2025-11-09
version: 1.0.0
"""

from chess.domain import DomainException
from chess.system import FinderException

__all__ = [
    "DomainVisitorFinderException",
    "ResidentSearchIdCollisionException",
    "ResidentSearchNameCollisionException",
    "ResidentSearchCoordCollisionException"
]


class DomainVisitorFinderException(DomainException, FinderException):
    """Base class for all DomainResidentFinder exception"""
    ERROR_CODE = "DOMAIN_VISITOR_SEARCH_ERROR"
    DEFAULT_MESSAGE = "DomainResidentFinder raised an exception."


class ResidentSearchIdCollisionException(DomainVisitorFinderException):
    """"""
    ERROR_CODE = "VISITOR_SEARCH_ID_COLLISION_ERROR"
    DEFAULT_MESSAGE = (
        "The DomainResidentFinder result had more than one result on a piece_id that should be unique. "
        "There may be inconsistent data in the system."
    )


class ResidentSearchNameCollisionException(DomainVisitorFinderException):
    """"""
    ERROR_CODE = "VISITOR_SEARCH_NAME_COLLISION_ERROR"
    DEFAULT_MESSAGE = (
        "The DomainResidentFinder result had more than one result on a piece_name that should be unique. "
        "There may be inconsistent data in the system."
    )


class ResidentSearchCoordCollisionException(DomainVisitorFinderException):
    """"""
    ERROR_CODE = "VISITOR_SEARCH_COORD_COLLISION_ERROR"
    DEFAULT_MESSAGE = (
        "The DomainResidentFinder result had more than one result on a piece.current_position that should be unique. "
        "There may be inconsistent data in the system."
    )
