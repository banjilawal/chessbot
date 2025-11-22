# src/chess/system/search/context/exception.py

"""
Module: chess.system.search.context.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ContextException


__all__ = ["SearchContextException",]

class SearchContextException(ContextException):
  """
  Super class for exceptions raised by SearchContext objects. DO NOT
  USE DIRECTLY. Subclasses give more useful debugging messages.
  """
  ERROR_CODE = "SEARCH_CONTEXT_ERROR"
  DEFAULT_MESSAGE = "SearchContext raised an exception."

 