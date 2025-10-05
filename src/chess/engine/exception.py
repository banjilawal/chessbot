

__all__ = [
  'EngineException',
# === ENGINE VALIDATION EXCEPTIONS ===
  'NullEngineException',
# === ENGINE BUILD EXCEPTIONS ===
  'BuildFailedException'
]

from chess.system import ChessException, NullException, BuildFailedException

class EngineException(ChessException):
  """
  Super class of exceptions organic to `Engine` objects. DO NOT USE DIRECTLY. Subclasses give
  details useful for debugging. `EngineException` exists primarily to allow catching all `Engine`
  exceptions.
  """
  ERROR_CODE = "ENGINE_ERROR"
  DEFAULT_MESSAGE = "Engine raised an exception."

class NullEngineException(EngineException, NullException):
  """Raised if an entity, method, or operation requires an `Engine` but gets null instead."""
  ERROR_CODE = "NULL_ENGINE_ERROR"
  DEFAULT_MESSAGE = "Engine cannot be null"

class EngineBuildFailed(EngineException, BuildFailedException):
  """
  Raised when `EngineBuilder` crashed while building a new object. Exists
  primarily to catch all exceptions raised creating engines.
  """
  ERROR_CODE = "ENGINE_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "Engine build failed."