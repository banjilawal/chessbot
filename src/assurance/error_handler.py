import logging
from typing import Callable, TypeVar, Any
from functools import wraps

T = TypeVar('T')

class ErrorHandler:
    def __init__(self, logger: logging.Logger = None):
        self.logger = logger or logging.getLogger(__name__)

    def __call__(self, func: Callable[..., T]) -> Callable[..., T]:
        """Decorator that captures and logs errors"""
        @wraps(func)
        def wrapper(*args, **kwargs) -> T:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                self._log_error(e, func, args[0] if args else None)
                raise  # Re-raise to preserve stack trace

        return wrapper

    def _log_error(self, error: Exception, func: Callable, instance: Any = None):
        """Extracts only class/method name and error details"""
        class_name = instance.__class__.__name__ if instance else "Module"
        method_name = func.__name__

        self.logger.error(
            "[%s.%s] %s: %s",
            class_name,
            method_name,
            error.__class__.__name__,  # Error type only
            str(error)                 # Error message only
            # No stacktrace, no context - error object is source of truth
        )