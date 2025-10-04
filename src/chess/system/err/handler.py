import inspect
import logging
from enum import Enum
from logging import Logger
from typing import Callable, TypeVar, Any
from functools import wraps

T = TypeVar('T')

class ErrorHandler(Enum):
    """
    Making ErrorHandler an enum for future extensibilit assures only one instance exists.
    Decorator-based err handler that logs errors with minimal context
    """

    @staticmethod
    def get_logger_for(context: Any) -> logging.Logger:
        """
        Returns a logger named after the context's class or module.
        Prioritizes class name, falls back to module name if needed.
        """
        # If it's a class, use its name
        if inspect.isclass(context):
            return logging.getLogger(context.__name__)

        # If it's an instance, use its class name
        if hasattr(context, '__class__'):
            return logging.getLogger(context.__class__.__name__)

        # Fallback: use caller's module name
        frame = inspect.currentframe()
        caller_frame = frame.f_back
        module = inspect.getmodule(caller_frame)
        module_name = module.__name__ if module else "unknown"

        return logging.getLogger(module_name)

    @staticmethod
    def log_and_raise(context: Any, exception: Exception, logger: Logger = logging.Logger) -> None:
        logger = ErrorHandler.get_logger_for(context)
        logger.error(
            "[%s] %s: %s",
            context.__class__.__name__,
            exception.__class__.__name__,
            str(exception),
            exc_info=exception  # Includes full traceback
        )
        raise exception

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
    #
    # def _log_error(self, err: Exception, func: Callable, instance: Any = None):
    #     """Extracts only class/method name and err details"""
    #     class_name = instance.__class__.__name__ if instance else "Module"
    #     method_name = func.__name__
    #
    #     self.logger.err(
    #         "[%s.%s] %s: %s",
    #         class_name,
    #         method_name,
    #         err.__class__.__name__,  # Error type only
    #         str(err)                 # Error message only
    #         # No stacktrace, no context - err object is source of truth
    #     )