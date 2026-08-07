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
        1.  Run checks making sure granting a Request does not introduce inconsistencies or failures.

    Attributes:
        priming_validator: PrimingValidator

    Provides:
        -    def execute(self, request: Request) -> RequestDecision

    Super Class:
    """
    
    _bootstrapper: Optional[PrimingValidator]
    
    def __init__(self, bootstrapper: Optional[PrimingValidator] | None = None):
        self._bootstrapper = bootstrapper or PrimingValidator()
        
    @property
    def bootstrapper(self) -> PrimingValidator:
        return self._bootstrapper
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> RequestDecision:
        pass