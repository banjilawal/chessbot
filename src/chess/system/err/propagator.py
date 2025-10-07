
from typing import Any, Callable, Optional
from chess.system import ErrorHandler, Result



class RaiserLogger:

  @staticmethod
  def propagate_error(context: Any, result: Optional[Result]=None, exception_factory: Callable[[], Exception]=None):
    if result is not None and result.is_success():
      return

    if exception_factory is None:
      exception_factory = RaiserLogger._default_exception_factory

    ErrorHandler.log_and_raise(context, exception_factory)


    # if not result.is_success():
    #   ErrorHandler.log_and_raise(roster, exception_factory)

  @staticmethod
  def _default_exception_factory(cls) -> Exception:
    return ValueError("There was an error propagating the error.")
