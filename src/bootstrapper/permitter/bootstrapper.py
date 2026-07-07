# src/permitter/push/permitter.py

"""
Module: permitter.push.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from abc import abstractmethod
from typing import Type

from bootstrapper import PrimingValidator
from err import PusherPermitterException, PushRequestNullException
from permitter import Permitter
from report import PushApprovalReport
from request import PushRequest
from result import ValidationResult
from util import LoggingLevelRouter


class PermitterBootstrapper:
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
    
    def __init__(
            self,
            priming_validator: PrimingValidator | None = PrimingValidator(),
    ):
        """
        Args:
            priming_validator: PrimingValidator
        """
        self._priming_validator = priming_validator
    
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._priming_validator
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def bootstrap_request(self, request) -> ValidationResult:
        pass