from enum import Enum
from typing import Any, Callable

from chess.system import Result, ErrorHandler


class RaiserLogger(Enum):
  @staticmethod
  def throw_if_invalid(context: Any, result: Result, exception_factory: Callable[[], Exception] = None):
    if result.is_success():
      return

    if exception_factory is None:
      exception_factory = RaiserLogger._default_exception_factory

    ErrorHandler.log_and_raise(context, exception_factory())

    # if not result.is_success():
    #   ErrorHandler.log_and_raise(roster, exception_factory)

  @staticmethod
  def _default_exception_factory() -> Exception:
    return ValueError("Validation failed")