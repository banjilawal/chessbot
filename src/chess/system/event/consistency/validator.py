from abc import ABC
from typing import Generic, Tuple, TypeVar

from chess.system import LoggingLevelRouter, ValidationResult, Validator

T = TypeVar('T')
X = TypeVar('X')

class BindingValidator(ABC, Generic[T, X]):
    """Base pattern for all consistency validators"""

    def __init__(self, element_validator: Validator[T], environment_validator: Validator[X]):
        self._element_validator = element_validator
        self._environment_validator = environment_validator


    @classmethod
    @abstractmethod
    @LoggingLevelRouter.monitor
    def validate_consistency(self, element: T, environment: E) -> ValidationResult[Tuple[T, X]]:
        """Validate consistency between element and its environment"""
        pass

    def validate(self, element: Any, environment: Any) -> ValidationResult[T]:
        """Standardized validation flow"""
        # 1. Validate environment
        env_result = self._environment_validator.validate(environment)
        if env_result.is_failure():
            return ValidationResult(exception=env_result.exception)

        # 2. Validate element
        element_result = self._element_validator.validate(element)
        if element_result.is_failure():
            return ValidationResult(exception=element_result.exception)

        # 3. Validate consistency (implemented by subclasses)
        return self.validate_consistency(element_result.payload, env_result.payload)