# src/authorization/adjudicator/chain/add/adjudicator.py

"""
Module: authorization.adjudicator.chain.add.adjudicator
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar

from assurance import PrimingValidator
from authorization import ChainRequestAdjudicator
from util import LoggingLevelRouter



T = TypeVar("T", bound="NodeAdditionRequest")

class NodeAdditionRequestAdjudicator(ChainRequestAdjudicator, ABC, Generic[T]):
    
    def __init__(self, bootstrapper: Optional[PrimingValidator] | None = None):
        super().__init__(bootstrapper=bootstrapper)

    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> NodeAdditionApprovalReport:
        pass