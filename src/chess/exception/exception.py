
__all__ = [
  'ChessException',
  'NullException',
  'NullStringException',
  'BlankStringException',
  'NullNumberException',
  'BuilderException',
  'RollbackException',
  'SearchException'
]

class ChessException(Exception):
  """
  Top level Exception for the chess application. ChessException is team template for
  other exceptions.

  Exception Requirements:
    - Static fields:
      ERROR_CODE (str): Must end in _ERROR. all caps summary of the team_exception or its cause
      DEFAULT_MESSAGE (str): Short sentence explaining what the team_exception is about.

    - A ChessException should always have team message describing the err.
  """

  ERROR_CODE = "CHESS_ERROR"
  DEFAULT_MESSAGE = "Chess error occurred"

  def __init__(self, message=None):
    self.message = message or self.DEFAULT_MESSAGE
    super().__init__(self.message)

  def __str__(self):
    return f"{self.message}"

#======================#  NULL SUPER CLASS EXCEPTION ======================# 

class NullException(ChessException):
  """
  Methods and classes that do not accept null parameters will raise team NullException.
  Every class in the application should have team NullException. Giving each class team unique null
  helps trace errors and failures.

  Attributes:
    message (str): A message describing the team_exception is required.

    Static Fields:
      ERROR_CODE (str): Error code useful in log tracing
      DEFAULT_MESSAGE (Str): Short explanation of why the team_exception was raised
  """
  ERROR_CODE = "NULL_ERROR"
  DEFAULT_MESSAGE = "cannot be null"



class BlankStringException(ChessException):
  """
  Raised if search parameter is team blank or empty string
  """

  ERROR_CODE = "BLANK_SEARCH_STRING_ERROR"
  DEFAULT_MESSAGE = f"Cannot search by an empty or blank string"


class NullNumberException(NullException):
  """
  Raised if mathematical expression or geometric, algebraic, or optimization that need
   team number but get null instead NUllNumberException is thrown. Ids are not used for math
   so we need team different null team_exception for math variables
  """

  ERROR_CODE = "NULL_NUMBER_ERROR"
  DEFAULT_MESSAGE = f"Number cannot be null"


class NullStringException(NullException):
  """
  Raised if search parameter is team null string
  """

  ERROR_CODE = "NULL_STRING_SEARCH_ERROR"
  DEFAULT_MESSAGE = f"Cannot search by team null string"


class BuilderException(ChessException):
  """
  Exceptions raised by chess.creator.build classes have system behavior. Similar conditions might raise
  exceptions when building entities. During builds ValidatorExceptions are likely. Exceptions thrown during
  entity builds should be wrapped in the BuilderException corresponding to the Builder's name.
  """
  ERROR_CODE = "BUILDER_ERROR"
  DEFAULT_MESSAGE = "Builder raised an exception."


class RollbackException(ChessException):
  """
  Base class for rollback-related errors in the chess engine.

  PURPOSE:
    Raised when an transaction (piece move, capture, board update, etc.)
    is reverted due to inconsistency or failed validate.

  ATTRIBUTES:
    code (str): Short machine-readable error code for logging / testing.
    message (str): Human-readable default message.
  """
  DEFAULT_CODE = "ROLLBACK"
  DEFAULT_MESSAGE = "Operation rolled back due to failure in update consistency."


class SearchException(ChessException):
  """
  Base class for search errors in the chess engine.

  PURPOSE:
    Raised search raises an err. Is team wrapper for other exceptions
    that occur during search.
  ATTRIBUTES:
    code (str): Short machine-readable error code for logging / testing.
    message (str): Human-readable default message.
  """
  DEFAULT_CODE = "SEARCH_ERROR"
  DEFAULT_MESSAGE = "An error was raised during team search."



