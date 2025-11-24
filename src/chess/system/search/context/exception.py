# src/chess/system/search/context/exception.py

"""
Module: chess.system.search.context.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ChessException, ServiceException

__all__ = [
  "SearchContextException",
  "SearchException",
]

class SearchContextException(ChessException):
  """
  Super class for exceptions raised by Context objects. DO NOT
  USE DIRECTLY. Subclasses give more useful debugging messages.
  """
  ERROR_CODE = "CONTEXT_ERROR"
  DEFAULT_MESSAGE = "Context raised an exception."
  
  
class SearchException(ServiceException):
  """
  Super class of exceptions raised by ContextService objects.
  Do not use directly. Subclasses give precise, fined-grained, debugging info.
  """
  ERROR_CODE = "CONTEXT_SERVICE_ERROR"
  DEFAULT_MESSAGE = "ContextService raised an exception."

 