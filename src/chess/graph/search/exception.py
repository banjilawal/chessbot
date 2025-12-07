# src/chess/domain/searcher/exception

"""
Module: chess.domain.searcher.exception
Author: Banji Lawal
Created: 2025-11-09
version: 1.0.0
"""

from chess.domain import DomainException
from chess.system import SearchException

__all__ = [
    "DomainVisitorSearchException",
    "VisitorSearchIdCollisionException",
    "VisitorSearchNameCollisionException",
    "VisitorSearchCoordCollisionException"
]


class DomainVisitorSearchException(DomainException, SearchException):
    """Base class for all DomainResidentSearch exceptions"""
    ERROR_CODE = "DOMAIN_VISITOR_SEARCH_ERROR"
    DEFAULT_MESSAGE = "DomainResidentSearch raised an exception."


class VisitorSearchIdCollisionException(DomainVisitorSearchException):
    """"""
    ERROR_CODE = "VISITOR_SEARCH_ID_COLLISION_ERROR"
    DEFAULT_MESSAGE = (
        "The DomainResidentSearch result had more than one result on a piece_id that should be unique. "
        "There may be inconsistent data in the system."
    )


class VisitorSearchNameCollisionException(DomainVisitorSearchException):
    """"""
    ERROR_CODE = "VISITOR_SEARCH_NAME_COLLISION_ERROR"
    DEFAULT_MESSAGE = (
        "The DomainResidentSearch result had more than one result on a piece_name that should be unique. "
        "There may be inconsistent data in the system."
    )


class VisitorSearchCoordCollisionException(DomainVisitorSearchException):
    """"""
    ERROR_CODE = "VISITOR_SEARCH_COORD_COLLISION_ERROR"
    DEFAULT_MESSAGE = (
        "The DomainResidentSearch result had more than one result on a piece.current_position that should be unique. "
        "There may be inconsistent data in the system."
    )
