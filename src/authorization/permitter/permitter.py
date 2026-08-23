# src/authorization/permitter/permitter.py

"""
Module: authorization.permitter.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

from assurance import PrimingValidator
from authorization import Request, RequestAdjudicator
from artifcat.report import AuthorizationDecision
from util import LoggingLevelRouter


T = TypeVar("T", bound="Result")


class OperationPermitter(ABC, Generic[T]):
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
    _adjudicator: RequestAdjudicator
    _priming_validator: PrimingValidator
    
    def __init__(
            self,
            adjudicator: RequestAdjudicator,
            priming_validator: Optional[PrimingValidator] |  None = None,
    ):
        """
        Args:
            adjudicator: Adjudicator,
            priming_validator: Optional[PrimingValidator]
        """
        self._adjudicator = adjudicator
        self._priming_validator = priming_validator or PrimingValidator()

    @property
    def adjudicator(self) -> RequestAdjudicator:
        return self._adjudicator
        
    @property
    def priming_validator(self) -> PrimingValidator:
        return self._priming_validator
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: Request) -> AuthorizationDecision:
        pass