# src/chess/system/err/propagator
"""
Module: chess.system.err.propagator
Author: Banji Lawal
Created: 2025-09-28

# SCOPE:
* The limits of the module, defined by what it does not do.
* Where to look for related features this models does not provide because of its limitations.

# THEME:
* Highlight the core feature (thread-safety)
* Explain the how-and-why of implementation choices.

# PURPOSE:
* Function and role in the system.
* Why the module exists in the application architecture
* What problem it fundamentally solves

# DEPENDENCIES:

# CONTAINS:
 * `OccupationTransaction`
"""
from functools import wraps
from typing import Any, Callable, Optional, TypeVar
from chess.system import LogWriter, Result

T = TypeVar("T")

class LoggingLevelRouter:
  """
  ROLE:
  ----
  RESPONSIBILITIES:
  ----------------
  1. Cut down logging boilerplate by centralizing and unifying
      the routing of successes or failures to either th error or
      info logs.
  2. Can be used directly in the code body, or as a decorator.

  ATTRIBUTES:
  ----------
  None
  """

  @staticmethod
  def route_error(
      context: Any,
      result: Optional[Any]=None,
      exception: Optional[Exception]=None,
      exception_factory: Optional[Callable[[], Exception]]=None
  ):
    """
    Writes errors from any source to the logger then re-raise it.
    e source
    for handling, wrapping.
    Ensures uniform logging without repetitive try/except.
    Arguments:
      * `context`:
      * `result`: Anything `context` is returning on success.
      * `exception`:
      * `exception_factory`:
    Returns:
      `void`
    Raises:
      None
    """

    if exception is not None:
      ex = exception
    elif result is not None and hasattr(result, 'exception'):
      ex = result.exception
    elif exception_factory is not None:
      ex = exception_factory()
    else:
      ex = ValueError("Unknown error source.")

    LogWriter.log_error(context, ex)
    raise ex

  @staticmethod
  def log_success(context: Any, message: str) -> None:
    LogWriter.log_info(context, message)


  @staticmethod
  def monitor(context: Any=None):
    """
    Decorator that automatically logs:
     - success as info
     - errors as error
    Works on instance/class methods or free functions.
    """
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
      @wraps(func)
      def wrapper(*args: Any, **kwargs: Any) -> T:
        actual_context = context or (args[0] if args else func)
        method_name = func.__name__
        try:
          result = func(*args, **kwargs)
          LogWriter.log_info(actual_context, f"{method_name} succeeded")
        except Exception as e:
          LogWriter.log_error(actual_context, e)
          raise
    return decorator