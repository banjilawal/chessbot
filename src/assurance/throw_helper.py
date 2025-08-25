from enum import Enum
from typing import Any, Callable

from assurance.error_handler import ErrorHandler
from assurance.result.base_result import Result


class ThrowHelper(Enum):
    @staticmethod
    def throw_if_invalid(context: Any, result: Result, exception_factory: Callable[[], Exception]):
        if result.is_success():
            return

        if exception_factory is None:
            exception_factory = ThrowHelper._default_exception_factory

        ErrorHandler.log_and_raise(context, exception_factory())

        # if not result.is_success():
        #     ErrorHandler.log_and_raise(context, exception_factory)

    @staticmethod
    def _default_exception_factory() -> Exception:
        return ValueError("Validation failed")
