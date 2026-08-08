# src/authorization/adjudicator/adjudicator.py

"""
Module: authorization.adjudicator.adjudicator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar

from assurance import PrimingValidator
from report import RequestDecision
from util import LoggingLevelRouter


T = TypeVar("T", bound="Request")

class RequestAdjudicator(ABC, Generic[T]):
    """
    Role:
        -   Permission Authorization
        -   Checklist Runner
        -   Integrity Maintenance
        _   Consistency Assurance

    Responsibilities:
        1.  Run safety checks on a Request.

    Attributes:
        priming_validator: PrimingValidator

    Provides:
        -    def execute(self, candidate: Any) -> RequestDecision

    Super Class:
    """
    
    _priming_validator: Optional[PrimingValidator]
    
    def __init__(self, priming_validator: Optional[PrimingValidator] | None = None):
        self._priming_validator = priming_validator or PrimingValidator()
        
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._priming_validator
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> RequestDecision:
        pass