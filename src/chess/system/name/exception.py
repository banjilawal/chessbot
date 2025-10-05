from chess.system import ChessException, NullException, ValidationException

__all__ = [
  'NullNameException',
  'LongNameException',
  'ShortNameException',
  'BlankNameException',
  'InvalidNameException',
]

from chess.system.err.exception import BlankStringException


class InvalidNameException(ValidationException):
  ERROR_CODE = "NAME_VALIDATION_ERROR"
  DEFAULT_MESSAGE = f"Name Validation failed"

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
  Name is longer than MAX_NAME_LENGTH raises LongNameException. See documentation
  pr chess.system.config for MAX_NAME_LENGTH
  """
  ERROR_CODE = "LONG_NAME_ERROR"
  DEFAULT_MESSAGE = "Name is above the maximum length"


class NullNameException(InvalidNameException, NullException):
  """
  Raised if an entity's name is null
  """
  ERROR_CODE = "NULL_NAME_ERROR"
  DEFAULT_MESSAGE = f"Name cannot be null"

