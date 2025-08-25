import logging
from enum import Enum
from logging import Logger
from typing import Callable, TypeVar, Any
from functools import wraps

T = TypeVar('T')

class ErrorHandler(Enum):
    """
    Making ErrorHandler an enum for future extensibilit assures only one instance exists.
    Decorator-based error handler that logs errors with minimal context
    """
    # def __init__(self, logger: logging.Logger = None):
    #     self.logger = logger or logging.getLogger(__name__)

    # def wrap(self, func: Callable[..., T], logger: logging.Logger) -> Callable[..., T]:
    #     """Decorator that captures and logs errors"""
    #     @wraps(func)
    #     def wrapper(*args, **kwargs) -> T:
    #         try:
    #             return func(*args, **kwargs)
    #         except Exception as e:
    #             self._log_error(e, func, args[0] if args else None)
    #             raise  # Re-raise to preserve stack trace
    #
    #     return wrapper

    @staticmethod
    def wrap(func: Callable[..., T], logger: logging.Logger) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> T:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                class_name = args[0].__class__.__name__ if args else "Module"
                method_name = func.__name__
                logger.error(
                    "[%s.%s] %s: %s",
                    class_name,
                    method_name,
                    e.__class__.__name__,
                    str(e)
                )
                raise
        return wrapper
    #
    # def _log_error(self, error: Exception, func: Callable, instance: Any = None):
    #     """Extracts only class/method name and error details"""
    #     class_name = instance.__class__.__name__ if instance else "Module"
    #     method_name = func.__name__
    #
    #     self.logger.error(
    #         "[%s.%s] %s: %s",
    #         class_name,
    #         method_name,
    #         error.__class__.__name__,  # Error type only
    #         str(error)                 # Error message only
    #         # No stacktrace, no context - error object is source of truth
    #     )