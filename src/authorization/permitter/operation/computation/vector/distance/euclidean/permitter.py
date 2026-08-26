# src/authorization/permitter/permitter.py

"""
Module: authorization.permitter.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Optional, cast

from assurance import PrimingValidator
from authorization import ComputationRequest
from artifcat.report import AuthorizationDecision
from util import LoggingLevelRouter




class EuclideanDistancePermitter(ComputationPermitter[VectorToggle]):
    """
    Role:
        -  Permission Authorization
        -  Integrity Maintenance
        _   Consistency Assurance

    Responsibilities:
        1.  Handoff service requests to the adjudicator to run through its authorization checklist.
        2.  Supply adjudicator dependencies.
        3.  Wrap any exceptions adjudicator exceptions for debuggung the exception chain.
        4.  Cast to the approrpate Request type before forwarding Adjudicator approvals to the client

    Attributes:
        adjudicator: EuclideanDistanceRequestAdjudicator
        priming_validator: PrimingValidator
        
    Provides:
        -   def execute(self, EuclideanDistanceRequest) -> RequestDecision

    Super Class:
        ComputationPermitter
    """
    
    def __init__(
            self,
            adjudicator: EuclideanDistanceRequestAdjudicator |  None = None,
            priming_validator: Optional[PrimingValidator] |  None = None,
    ):
        """
        Args:
            adjudicator: Optional[EuclideanDistanceRequestAdjudicator]
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(
            priming_validator=priming_validator,
            adjudicator=adjudicator or EuclideanDistanceRequestAdjudicator()
        )

    @property
    def adjudicator(self) -> EuclideanDistanceRequestAdjudicator:
        return cast(EuclideanDistanceRequestAdjudicator, super().adjudicator)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: EuclideanDistanceRequest) -> AuthorizationDecision:
        pass