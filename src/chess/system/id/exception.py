# src/chess/system/id/exception.py

"""
Module: chess.system.id.exception
Author: Banji Lawal
Created: 2025-09-17
Updated: 2025-10-10
version: 1.0.0
"""


from chess.system import ValidationException, NullException


__all__ = [
  'InvalidIdException',
  'IdNullException',
  'NegativeIdException'
]

class InvalidIdException(ValidationException):
  """
  Super class of exceptions raised by `IdValidator`. Subclasses give details useful for
  debugging. Exists primarily to allow catching and wrapping all errors discovered validating ids.
  DO NOT USE DIRECTLY.
  """
  ERROR_CODE = "ID_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Id Validation failed."

class IdNullException(NullException):
  """
  Raised if an entity's id is null
  """
  ERROR_CODE = "NULL_ID_ERROR"
  DEFAULT_MESSAGE = "Id cannot be null."


class NegativeIdException(InvalidIdException):
  """Raised if an id is zero or less"""
  ERROR_CODE = "ID_IS_NEGATIVE"
  DEFAULT_MESSAGE = "Id cannot be negative."


