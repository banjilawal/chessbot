# src/chess/neighbor/search/exception.py

"""
Module: chess.neighbor.search.exception
Author: Banji Lawal
Created: 2025-11-05
version: 1.0.0
"""


from chess.system import ChessException, SearchCollisionException

__all__ = [
  'VisitationSearchException',

#======================# SEARCH_COLLISION EXCEPTIONS #======================#
  'VisitationSearchCollisionException',
  'VisitationSearchIdCollisionException',
  'VisitationSearchNameCollisionException',
  'VisitationSearchCoordCollisionException',

  'SquareSearchIdCollisionException',
  'SquareSearchNameCollisionException',
  'SquareSearchCoordCollisionException',

  'TeamSearchIdCollisionException'
]

class VisitationSearchException(ChessException):
  """
  Super class of exceptions organic to `Search` objects. DO NOT USE DIRECTLY. Subclasses give
  details useful for debugging. `SearchException` exists primarily to allow catching all `Search`
  exceptions.
  """
  DEFAULT_CODE = "SEARCH_ERROR"
  DEFAULT_MESSAGE = "Search raised an rollback_exception."


#======================# SEARCH_COLLISION EXCEPTIONS #======================#
class VisitationSearchCollisionException(VisitationSearchException, SearchCollisionException):
  DEFAULT_CODE = "VISITATION_SEARCH_COLLISION_ERROR"
  DEFAULT_MESSAGE = (
    "VisitationSearch results contains records with multiple records with properties that should be unique. There "
    "may be service inconsistencies."
  )


class VisitationSearchIdCollisionException(VisitationSearchCollisionException):
  DEFAULT_CODE = "VISITATION_SEARCH_ID_COLLISION_ERROR"
  DEFAULT_MESSAGE = (
    "VisitationSearch results contains has more than one consistency for the piece_id which should be unique. There "
    "may be service inconsistencies."
  )

class VisitationSearchNameCollisionException(VisitationSearchCollisionException):
  DEFAULT_CODE = "VISITATION_SEARCH_NAME_COLLISION_ERROR"
  DEFAULT_MESSAGE = (
    "VisitationSearch results contains has more than one consistency for visitation_name, which should be unique. There "
    "may be service inconsistencies."
  )

class VisitationSearchCoordCollisionException(VisitationSearchCollisionException):
  DEFAULT_CODE = "VISITATION_SEARCH_COORD_COLLISION_ERROR"
  DEFAULT_MESSAGE = (
    "VisitationSearch results contains has more than one consistency for visitation_position, which should be unique. There "
    "may be service inconsistencies."
  )


class SquareSearchIdCollisionException(SearchCollisionException):
  DEFAULT_CODE = "SQUARE_SEARCH_ID_COLLISION_ERROR"
  DEFAULT_MESSAGE = (
    "More than one Square found with the same visitor_id. There may be a service inconsistency."
  )


class SquareSearchNameCollisionException(SearchCollisionException):
  DEFAULT_CODE = "SQUARE_SEARCH_NAME_COLLISION_ERROR"
  DEFAULT_MESSAGE = (
    "More than one Square found with the same visitor_name. There may be a service collision"
  )

class SquareSearchCoordCollisionException(SearchCollisionException):
  DEFAULT_CODE = "SQUARE_SEARCH_COORD_COLLISION_ERROR"
  DEFAULT_MESSAGE = (
    "More than one Square found at the same coordinate. There may be a service inconsistency."
  )

class TeamSearchIdCollisionException(SearchCollisionException):
  DEFAULT_CODE = "TEAM_SEARCH_ID_COLLISION_ERROR"
  DEFAULT_MESSAGE = (
    "More than one Team found with the same visitor_name. There may be a service inconsistency."
  )












