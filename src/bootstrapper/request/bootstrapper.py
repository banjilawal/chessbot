# src/permitter/push/permitter.py

"""
Module: permitter.push.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from typing import Any, Type

from err import NullException
from artifcat.result import ValidationResult
from util import LoggingLevelRouter
from assurance.validator import PrimingValidator


class RequestBootstrapper:
    """
    Role:
        - Analysis Worker
        - Consistency, Integrity Maintenance

    Responsibilities:
        1.  Checks if an object satisfies the conditions to perform an operation.

    Attributes:

    Provides:
        -   def execute(cls, requestor: T, *args, **kwargs) -> AnalysisResult

    Super Class:
        Permitter
    """
    _priming_validator: PrimingValidator
    
    def __init__(self, priming_validator: PrimingValidator | None = None,):
        """
        Args:
            priming_validator: PrimingValidator
        """
        self._priming_validator = priming_validator or PrimingValidator()
    
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._priming_validator
    

    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Any,
            request_model: Type[T],
            null_exception: NullException,
    ) -> ValidationResult:
        pass