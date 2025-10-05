from chess.exception import ChessException, ValidationException, NullException

__all__ = [
  'IdNullException',
  'NegativeIdException',
  'InvalidIdException'
]

class InvalidIdException(ValidationException):
  ERROR_CODE = "ID_VALIDATION_ERROR"
  DEFAULT_MESSAGE = f"Id Validation failed"

class IdNullException(NullException):
  """
  Raised if an entity's id is null
  """
  ERROR_CODE = "NULL_ID_ERROR"
  DEFAULT_MESSAGE = f"Id cannot be null"


class NegativeIdException(ChessException):
  ERROR_CODE = "ID_IS_NEGATIVE"
  DEFAULT_MESSAGE = "Id cannot be negative"


