# chess/agenet/search/exception.py

"""
Module: chess.board.search.exception
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

from chess.exception import ChessException

__all__ = [
  'ResultException',
  'ResultConstructorException',
  'EmptyResultConstructorException',
  'ErrorContradictsPayloadException'
]

class ResultException(ChessException):
  """Base class for all Result exceptions"""
  ERROR_CODE = "RESULT_ERROR"
  DEFAULT_MESSAGE = "Result raised an rollback_exception."


class ResultConstructorException(ResultException):
  """Base class for all Result exceptions"""
  ERROR_CODE = "RESULT_CONSTRUCTOR_ERROR"
  DEFAULT_MESSAGE = "Invalid constructor params raised an rollback_exception."


class EmptyResultConstructorException(ResultConstructorException):
  ERROR_CODE = "EMPTY_RESULT_CONSTRUCTOR_ERROR"
  DEFAULT_MESSAGE = "A Result cannot be constructed with no payload or err."


class ErrorContradictsPayloadException(ResultConstructorException):
  """Raised if both payload and error params are not null when constructing team_name Result object"""
  ERROR_CODE = "ERROR_CONFLICTS_PAYLOAD_IN_RESULT_CONSTRUCTOR"
  DEFAULT_MESSAGE = (
    "A Result cannot have both its payload and error set. Construct with either payload or err"
  )







