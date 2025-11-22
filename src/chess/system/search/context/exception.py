# src/chess/system/search/context/exception.py

"""
Module: chess.system.search.context.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ContextException, ServiceException

__all__ = [
  "SearchContextException",
  "SearchContextServiceException",
]

class SearchContextException(ContextException):
  """
  Super class for exceptions raised by SearchContext objects. DO NOT
  USE DIRECTLY. Subclasses give more useful debugging messages.
  """
  ERROR_CODE = "SEARCH_CONTEXT_ERROR"
  DEFAULT_MESSAGE = "SearchContext raised an exception."
  
  
class SearchContextServiceException(ServiceException):
  """
  Super class of exceptions raised by CoordContextService objects.
  Do not use directly. Subclasses give precise, fined-grained, debugging info.
  """
  ERROR_CODE = "COORD_CONTEXT_SERVICE_ERROR"
  DEFAULT_MESSAGE = "CoordContextService raised an exception."

 