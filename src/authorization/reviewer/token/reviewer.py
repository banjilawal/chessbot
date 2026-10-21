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
from authorization import ApplicantReviewer, AuthorizationLoader
from domain import Token
from err import TokenApproverException
from exchange import AuthorizationRequest, TokenValidationRequest, TokenValidationService
from transit import TokenCarrier
from util import IdFactory, LoggingLevelRouter

T = TypeVar("T", bound="AuthorizationRequest")

class ApplicantTokenReviewer(ApplicantReviewer[Token], ABC, Generic[T]):
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
            validation_checker: Optional[ValidTokenChecker] | None = None,
    ):
        """
        Args:
            loader: AuthorizationLoader[T]
            validation_service: TokenValidationService
        """
        super().__init__(validation_service=validation_service)
        self._loader = loader
        
    @property
    def loader(self) -> AuthorizationLoader[T]:
        return self._loader
        
    @property
    def validation_service(self) -> TokenValidationService:
        return cast(TokenValidationService, super().validation_service)
    
    @property
    @abstractmethod
    def disability_checker(self) -> Decision[T]:
        pass
    
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
    
    @LoggingLevelRouter.monitor
    def run_validation_check(self, applicant: Any) -> ValidationResult[Token]:
        """
        Checks if an applicant Token is safe.

        Action:
            1.  Send an exception chain in the ValidationResult if the candidate gets
                flagged.
            2.  Otherwise, send the success result.
        Args:
            applicant: Any
        Returns:
           ValidationResult[Token]
        Raises:
            TokenApproverException
        """
        method = f"{self.__class__.__name__}.validation_check"
        
        # Handle the case that the candidate gets flagged.
        validation = self.validation_service.extract_model(
            request=TokenValidationRequest(
                item=TokenCarrier(model=applicant),
                id=IdFactory.next_id(class_name="TokenValidationRequest")
            )
        )
        if validation.is_failure:
            # Send the exception chain on failure.
            return ValidationResult.failure(
                TokenApproverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenApproverException.MSG,
                    err_code=TokenApproverException.ERR_CODE,
                )
            )
        # --- Forward the work product. ---#
        token = cast(Token, validation.payload)
        return ValidationResult.success(token)

    @abstractmethod
    @LoggingLevelRouter.monitor
    def run_applicant_readiness_check(self, applicant: T) -> Decision[T]:
        pass
        