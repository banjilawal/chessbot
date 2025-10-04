
from typing import Any, Callable

from chess.system import ErrorHandler, Result



class ErrorPropagator:
    
    @classmethod
    def propagate_error(cls, context: Any, result: Result, exception_factory: Callable[[], Exception] = None):
        if result.is_success():
            return

        if exception_factory is None:
            exception_factory = ErrorPropagator._default_exception_factory(result.exception)

        ErrorHandler.log_and_raise(context, exception_factory())

        # if not result.is_success():
        #     ErrorHandler.log_and_raise(context, exception_factory)

    @classmethod
    def _default_exception_factory(cls, exception: Exception) -> Exception:
        return exception
