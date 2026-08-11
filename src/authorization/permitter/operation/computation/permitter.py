# src/authorization/permitter/permitter.py

"""
Module: authorization.permitter.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

from assurance import PrimingValidator
from authorization import ComputationRequest, OperationPermitter
from report import RequestDecision
from util import LoggingLevelRouter


T = TypeVar("T")


class ComputationPermitter(OperationPermitter, ABC, Generic[T]):
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
        priming_validator: PrimingValidator
        
    Provides:
        -    def execute(self, request: Request) -> RequestDecision

    Super Class:
    """
    _adjudicator: ComputationRequestAdjudicator
    _priming_validator: PrimingValidator
    
    def __init__(
            self,
            adjudicator: ComputationRequestAdjudicator,
            priming_validator: Optional[PrimingValidator] |  None = None,
    ):
        """
        Args:
            adjudicator: ComputationRequestAdjudicator,
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(priming_validator=priming_validator, adjudicator=adjudicator)


    @property
    def adjudicator(self) -> ComputationRequestAdjudicator[T]:
        return self._adjudicator
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: ComputationRequest[T]) -> RequestDecision:
        pass