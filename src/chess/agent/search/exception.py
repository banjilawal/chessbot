# chess/agenet/search/exception.py

"""
Module: chess.agent.search.exception
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

from chess.system import SearchException

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


class TeamSearchIdCollisionException(TeamSearchException):
  """"""
  ERROR_CODE = "TEAM_SEARCH_ID_COLLISION_ERROR"
  DEFAULT_MESSAGE = (
    "TeamSearch produced multiple results with the same id. Team.id should be globally unique. There "
    "may be inconsistent data in the system."
  )
