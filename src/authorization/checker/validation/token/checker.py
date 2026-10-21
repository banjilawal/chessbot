# src/authorization/applicant/token/approver.py

"""
Module: authorization.applicant.token.approver
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import Decision, ValidationResult
from authorization import ApplicantApprover, AuthorizationLoader
from domain import Token
from err import TokenApproverException
from exchange import AuthorizationRequest, TokenValidationRequest, TokenValidationService
from transit import TokenCarrier
from util import IdFactory, LoggingLevelRouter

T = TypeVar("T", bound="AuthorizationRequest")

class ValidTokenChecker(ValidationChecker[Token]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks if a Token satisfies the requirements for an activity.

    Attributes:
        loader: AuthorizationLoader[T]
        validation_service: TokenValidationService

    Provides:
        -   def execute(request: T) -> Decision[T]
        -   def validation_check(applicant: Any) -> ValidationResult[Token]
        -   def load_check(request: Any, loader: AuthorizationLoader[T]) -> Decision[T]


    Super Class:
        ApplicantApprover
    """
    _loader: AuthorizationLoader[T]

    
    def __init__(
            self,
            loader: AuthorizationLoader[T],
            validation_service: TokenValidationService
    ):
        """
        Args:
            loader: AuthorizationLoader[T]
            validation_service: TokenValidationService
        """
        super().__init__(validation_service=validation_service)
        
    @property
    def validation_service(self) -> TokenValidationService:
        return cast(TokenValidationService, super().validation_service)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: AuthorizationRequest) -> Decision:
        """
        Checks if a Token meets the requirements to perform an activity.

        Args:
            request: AuthorizationRequest
        Returns:
           Decision
        Raises:
            TokenApproverException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate gets flagged.
        validation = self.validation_service.extract_model(
            request=TokenValidationRequest(
                item=TokenCarrier(model=request.applicant),
                id=IdFactory.next_id(class_name="TokenValidationRequest")
            )
        )
        if validation.is_failure:
            # Send the exception chain on failure.
            return Decision.denial(
                request=request,
                exception=TokenApproverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenApproverException.MSG,
                    err_code=TokenApproverException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        applicant = cast(Token, validation.payload)
        approval = AuthorizationRequest(
            id=request.id,
            activity=request.activity,
            applicant=applicant,
        )
        # --- Forward the work product. ---#
        return Decision.grant(approval)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def load_request(self, request: Any, loader: AuthorizationLoader[T], ) -> Decision[T]:
        """
        Loads the request into the TokenApprover

        Action:
            1.  Send a denial if the loader fails.
            2.  Otherwise, send an Approval.
        Args:
            request: Any
            loader: AuthorizationLoader[T]
        Returns:
           Decision[T]
        Raises:
            TokenApproverException
        """
        pass
 