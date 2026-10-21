# src/authorization/applicant/token/approver.py

"""
Module: authorization.applicant.token.approver
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from artifcat import Decision
from authorization import ApplicantApprover
from domain import Token
from exchange import AuthorizationRequest, TokenValidationService
from util import LoggingLevelRouter

T = TypeVar("T", bound="AuthorizationRequest")

class TokenApprover(ApplicantApprover[Token], ABC, Generic[T]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks if a Token satisfies the requirements for an activity.

    Attributes:
        validation_service: TokenValidationService

    Provides:
        -   def execute(request: T) -> Decision[T]

    Super Class:
        ApplicantApprover
    """

    
    def __init__(
            self,
            validation_service: Optional[TokenValidationService] | None = None
    ):
        """
        Args:
            validation_service: Optional[TokenValidationService]
        """
        super().__init__(
            validation_service=validation_service or TokenValidationService()
        )
        
    @property
    def validation_service(self) -> TokenValidationService:
        return cast(TokenValidationService, super().validation_service)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, request: T) -> Decision[T]:
        """
        Checks if a Token meets the requirements to perform an activity.

        Args:
            request: AuthorizationRequest[T]
        Returns:
           Decision[T]
        Raises:
            TokenApproverException
        """
        pass
        