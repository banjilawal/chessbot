# src/chess/agent/search/exception

"""
Module: chess.agent.search.exception
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

from chess.system import SearchException

__all__ = [
  # ======================# AGENT_SEARCH EXCEPTIONS #======================#
  "AgentSearchException",
]


# ======================# AGENT_SEARCH EXCEPTIONS #======================#
class AgentSearchException(SearchException):
  """
  Super class of exceptions raised by AgentSearch objects. Do not use directly. Subclasses give
  precise, fined-grained, debugging info.
  """
  ERROR_CODE = "AGENT_SEARCH_ERROR"
  DEFAULT_MESSAGE = "AgentSearch raised an exception."