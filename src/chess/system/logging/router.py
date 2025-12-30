# src/chess/system/logging/router.py

"""
Module: chess.system.router
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from functools import wraps
from typing import Any, Callable, Optional, TypeVar
from chess.system import LogWriter, Result

T = TypeVar("V")

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
  def log_and_raise_error(
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
      * `map`:
      * `notification`: Anything `map` is returning on success.
      * `rollback_exception`:
      * `exception_factory`:
    RETURNS:
      `void`
    RAISES:
      None
    """

    if exception is not None:
      ex = exception
    elif result is not None and hasattr(result, 'rollback_exception'):
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
        return wrapper
    return decorator