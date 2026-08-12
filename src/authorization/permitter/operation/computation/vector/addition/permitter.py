# src/authorization/permitter/permitter.py

"""
Module: authorization.permitter.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from assurance import PrimingValidator
from authorization import ComputationRequest, OperationPermitter
from report import AuthorizationDecision
from util import LoggingLevelRouter




class AddVectorPermitter(ComputationPermitter[VectorToggle]):
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
        adjudicator: AddVectorRequestAdjudicator
        priming_validator: PrimingValidator
        
    Provides:
        -    def execute(self, AddVectorRequest) -> RequestDecision

    Super Class:
        ComputationPermitter
    """
    
    def __init__(
            self,
            adjudicator: AddVectorRequestAdjudicator |  None = None,
            priming_validator: Optional[PrimingValidator] |  None = None,
    ):
        """
        Args:
            adjudicator: Optional[AddVectorRequestAdjudicator]
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(
            priming_validator=priming_validator,
            adjudicator=adjudicator or AddVectorRequestAdjudicator()
        )

    @property
    def adjudicator(self) -> AddVectorRequestAdjudicator:
        return cast(AddVectorRequestAdjudicator, super().adjudicator)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: AddVectorRequest) -> AuthorizationDecision:
        pass