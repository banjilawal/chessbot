# src/authorization/adjudicator/stack/adjudicator.py

"""
Module: authorization.adjudicator.stack.adjudicator
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar

from assurance import PrimingValidator
from authorization import RequestAdjudicator
from artifcat.report import StackOperationApprovalReport

from util import LoggingLevelRouter



T = TypeVar("T", bound="StackRequest")

class StackRequestAdjudicator(RequestAdjudicator, ABC, Generic[T]):
    
    def __init__(self, priming_validator: Optional[PrimingValidator] | None = None):
        super().__init__(priming_validator=priming_validator)

    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> StackOperationApprovalReport:
        pass