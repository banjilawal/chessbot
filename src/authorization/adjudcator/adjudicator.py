# src/core/adjudicator/adjudicator.py

"""
Module: core.adjudicator.adjudicator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar

from report import OperationApprovalReport
from util import LoggingLevelRouter
from assurance.validator import PrimingValidator


T = TypeVar("T", bound="Request")

class RequestAdjudicator(ABC, Generic[T]):
    
    _bootstrapper: Optional[PrimingValidator]
    
    def __init__(self, bootstrapper: Optional[PrimingValidator] | None = None):
        self._bootstrapper = bootstrapper or PrimingValidator()
        
    @property
    def bootstrapper(self) -> PrimingValidator:
        return self._bootstrapper
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> OperationApprovalReport:
        pass