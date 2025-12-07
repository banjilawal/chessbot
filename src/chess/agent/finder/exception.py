# src/chess/agent/searcher/exception

"""
Module: chess.agent.searcher.exception
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

from chess.system import FinderException

__all__ = [
  # ======================# AGENT_SEARCH EXCEPTIONS #======================#
  "AgentFinderException",
]


# ======================# AGENT_SEARCH EXCEPTIONS #======================#
class AgentFinderException(FinderException):
  """
  Super class of exceptions raised by AgentFinder objects. Do not use directly. Subclasses give
  precise, fined-grained, debugging info.
  """
  ERROR_CODE = "AGENT_SEARCH_ERROR"
  DEFAULT_MESSAGE = "AgentFinder raised an exception."