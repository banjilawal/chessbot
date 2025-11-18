# chess/agenet/search/exception.py

"""
Module: chess.agent.search.exception
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

from chess.system import InconsistencyException, SearchException

__all__ = [
  "TeamSearchException",
  "TeamSearchIdCollisionException",
]



class TeamSearchException(SearchException):
  """
  Super class of exceptions raised by TeamSearch objects. Do not use directly. Subclasses give
  precise, fined-grained, debugging info.
  """
  ERROR_CODE = "TEAM_SEARCH_ERROR"
  DEFAULT_MESSAGE = "TeamSearch raised an exception."


class TeamSearchIdCollisionException(TeamSearchException, InconsistencyException):
  """
  Raised if a search produced multiple results with the same id ad other properties do not match.
  This error is not raised by duplicates (all properties are the same.)
  """
  ERROR_CODE = "TEAM_SEARCH_ID_COLLISION_ERROR"
  DEFAULT_MESSAGE = (
    "TeamSearch produced multiple results with the same id but other properties do not match. Ids should "
    "be globally unique. If multiple Teams with all properties except the id differing, There may be data "
    "inconsistencies in the system."
  )
