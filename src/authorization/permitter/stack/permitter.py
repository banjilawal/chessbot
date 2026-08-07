# src/authorization/permitter/stack/permitter.py

"""
Module: authorization.permitter.stack.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from assurance import PrimingValidator
from authorization import OperationPermitter, Request, RequestAdjudicator, StackRequestAdjudicator
from report import RequestDecision
from util import LoggingLevelRouter


T = TypeVar("T", bound="StackRequest")


class StackOperationPermitter(OperationPermitter, ABC, Generic[T]):
    """
    Role:
        -   Permission Authorization
        -   Integrity Maintenance
        _   Consistency Assurance

    Responsibilities:
        1.  Handoff service requests to the adjudicator to run through its authorization checklist.
        2.  Supply adjudicator dependencies.
        3.  Wrap any exceptions adjudicator exceptions for debuggung the exception chain.
        4.  Cast to the approrpate Request type before forwarding Adjudicator approvals to the client

    Attributes:
            adjudicator: StackRequestAdjudicator,
            priming_validator: Optional[PrimingValidator]
        
    Provides:
        -    def execute(self, request: T) -> RequestDecision

    Super Class:
        OperationPermitter
    """
    _adjudicator: StackRequestAdjudicator[T]
    _priming_validator: PrimingValidator
    
    def __init__(
            self,
            adjudicator: StackRequestAdjudicator,
            priming_validator: Optional[PrimingValidator] |  None = None,
    ):
        """
        Args:
            adjudicator: StackRequestAdjudicator,
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(adjudicator=adjudicator, priming_validator=priming_validator)
        

    @property
    def adjudicator(self) -> StackRequestAdjudicator[T]:
        return cast(StackRequestAdjudicator[T], super().adjudicator)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> RequestDecision:
        pass