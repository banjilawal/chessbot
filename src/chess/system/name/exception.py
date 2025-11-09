# src/chess/system/name/exception.py

"""
Module: chess.system.name.exception
Author: Banji Lawal
Created: 2025-09-17
Updated: 2025-10-10
version: 1.0.0
"""

from chess.system import NullException, ValidationException, BlankStringException


__all__ = [
  'InvalidNameException',
  'BlankNameException',
  'ShortNameException',
  'LongNameException',
  'NullNameException',
]


class InvalidNameException(ValidationException):
  """
  Super class of exceptions raised by `NameValidator`. Subclasses give details useful for debugging. Exists primarily
  to allow catching and wrapping all errors discovered validating names. DO NOT USE DIRECTLY.
  """
  ERROR_CODE = "NAME_VALIDATION_ERROR"
  DEFAULT_MESSAGE = "Name validation failed"

class BlankNameException(InvalidNameException, BlankStringException):
  """
  Name with only white space raises BlankNameException
  """
  ERROR_CODE = "BLANK_NAME_ERROR"
  DEFAULT_MESSAGE = "Name cannot be white space only"


class ShortNameException(InvalidNameException):
  """
  Name below the minimum length raises ShortNameException. See documentation or
  chess.system.config for MIN_NAME_LENGTH.
  """
  ERROR_CODE = "SHORT_NAME_ERROR"
  DEFAULT_MESSAGE = "Name is below the minimum length"


class LongNameException(InvalidNameException):
  """
  Name is longer than MAX_NAME_LENGTH raises LongNameException.
  """
  ERROR_CODE = "LONG_NAME_ERROR"
  DEFAULT_MESSAGE = "Name is above the maximum length"


class NullNameException(InvalidNameException, NullException):
  """
  Raised if an entity's name is null
  """
  ERROR_CODE = "NULL_NAME_ERROR"
  DEFAULT_MESSAGE = f"Name cannot be null"

