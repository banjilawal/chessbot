from chess.exception import ChessException, NullException

__all__ = [
  'BuilderException',
  'NullBuilderException',
  'BuildFailedException'
]


class BuilderException(ChessException):
  """
  Super class of exceptions organic to `Builder` objects. DO NOT USE DIRECTLY. Subclasses give
  details useful for debugging. `BuilderException` exists primarily to allow catching all `Builder`
  exceptions.
  """
  ERROR_CODE = "BUILDER_ERROR"
  DEFAULT_MESSAGE = "Builder raised an exception."

class NullBuilderException(BuilderException, NullException):
  """Raised if an entity, method, or operation requires a Engine but gets null instead."""
  ERROR_CODE = "NULL_ERROR"
  DEFAULT_MESSAGE = "Builder cannot be null"

class BuildFailedException(BuilderException):
  """
  Raised when a Builder encounters an error while building an object. Exists primarily to
  catch all exceptions raised building a new objects.
  """
  ERROR_CODE = "BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "build failed."



