# src/authorization/checker/model/token/checker.py

"""
Module: authorization.checker.model.token.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import Decision
from authorization import ModelChecker
from domain import Token
from err import TokenApproverException
from exchange import AuthorizationRequest, TokenValidationRequest, TokenValidationService
from transit import TokenCarrier
from util import IdFactory, LoggingLevelRouter

class ValidTokenChecker(ModelChecker[Token]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Verifies a Token meets minimum safety requirements before it
            can be approved for an activity.

    Attributes:
        validation_service: TokenValidationService

    Provides:
        -   def execute(request: AuthorizationRequest) -> Decision

    Super Class:
        ModelChecker
    """
    
    def __init__(
            self,
            validation_service: Optional[TokenValidationService] | None = None,
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
 