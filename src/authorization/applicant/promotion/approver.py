# src/authorization/applicant/promotion/approver.py

"""
Module: authorization.applicant.promotion.approver
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from artifcat import PromotionDecision
from authorization import ApplicantApprover
from domain import Actor
from exchange import PromotionRequest, ValidationService
from util import LoggingLevelRouter

T = TypeVar("T", bound="Actor")

class PromotionApplicantApprover(ApplicantApprover[PromotionRequest], ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Reports if an Applicant satisfies the requirements for Promotion.

    Attributes:
        validation_service: ValidationService[T]

    Provides:
        -   def execute(request: PromotionRequest) -> PromotionDecision

    Super Class:
        ApplicantApprover
    """
    _validation_service: ValidationService[T]

    
    def __init__(self, validation_service: ValidationService[T]):
        """
        Args:
            validation_service: ValidationService[T]
        """
        super().__init__()
        self._validation_service = validation_service
        
    @property
    def validation_service(self) -> ValidationService[T]:
        return self.validation_service
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: PromotionRequest) -> PromotionDecision:
        pass
        