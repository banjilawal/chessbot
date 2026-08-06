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
from authorization import RequestAdjudicator
from util import LoggingLevelRouter



T = TypeVar("T", bound="LinkedListRequest")

class LinkedListRequestAdjudicator(RequestAdjudicator, ABC, Generic[T]):
    
    def __init__(self, bootstrapper: Optional[PrimingValidator] | None = None):
        super().__init__(bootstrapper=bootstrapper)

    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> LinkedListOperationApprovalReport:
        pass