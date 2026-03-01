# src/logic/points/searcher/exception

"""
Module: logic.points.searcher.exception
Author: Banji Lawal
Created: 2025-11-09
version: 1.0.0
"""

from logic.domain import DomainException
from logic.system import FinderException

__all__ = [
    "DomainVisitorFinderException",
    "VisitorSearchIdCollisionException",
    "VisitorSearchNameCollisionException",
    "VisitorSearchCoordCollisionException"
]


class DomainVisitorFinderException(DomainException, FinderException):
    """Base class for all DomainResidentFinder exception"""
    ERR_CODE = "DOMAIN_VISITOR_SEARCH_EXCEPTION"
    MSG = "DomainResidentFinder raised an exception."


class VisitorSearchIdCollisionException(DomainVisitorFinderException):
    """"""
    ERR_CODE = "VISITOR_SEARCH_ID_COLLISION_EXCEPTION"
    MSG = (
        "The DomainResidentFinder result had more than one result on a piece_id that should be unique. "
        "There may be inconsistent data in the system."
    )


class VisitorSearchNameCollisionException(DomainVisitorFinderException):
    """"""
    ERR_CODE = "VISITOR_SEARCH_NAME_COLLISION_EXCEPTION"
    MSG = (
        "The DomainResidentFinder result had more than one result on a piece_name that should be unique. "
        "There may be inconsistent data in the system."
    )


class VisitorSearchCoordCollisionException(DomainVisitorFinderException):
    """"""
    ERR_CODE = "VISITOR_SEARCH_COORD_COLLISION_EXCEPTION"
    MSG = (
        "The DomainResidentFinder result had more than one result on a piece.current_position that should be unique. "
        "There may be inconsistent data in the system."
    )
