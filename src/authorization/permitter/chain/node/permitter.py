# src/authorization/permitter/chain/permitter.py

"""
Module: authorization.permitter.chain.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from assurance import PrimingValidator
from authorization import OperationPermitter, ChainRequestAdjudicator
from report import AuthorizationDecision
from util import LoggingLevelRouter


T = TypeVar("T", bound="ChainRequest")


class ChainOperationPermitter(OperationPermitter, ABC, Generic[T]):
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
            adjudicator: ChainRequestAdjudicator,
            priming_validator: Optional[PrimingValidator]
        
    Provides:
        -    def execute(self, request: T) -> RequestDecision

    Super Class:
        ChainOperationPermitter
    """
    _adjudicator: ChainRequestAdjudicator[T]
    
    def __init__(
            self,
            adjudicator: ChainRequestAdjudicator[T],
            priming_validator: Optional[PrimingValidator] | None = None,
    ):
        """
        Args:
            adjudicator: ChainRequestAdjudicator[T],
            priming_validator: Optional[PrimingValidator]
        """
        super().__init__(adjudicator=adjudicator, priming_validator=priming_validator)
        

    @property
    def adjudicator(self) -> ChainRequestAdjudicator[T]:
        return cast(ChainRequestAdjudicator[T], super().adjudicator)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> AuthorizationDecision:
        pass