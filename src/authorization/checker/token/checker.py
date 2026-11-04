# src/authorization/checker/token/checker.py

"""
Module: authorization.checker.token.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import Decision
from domain import CombatantToken, KingToken, Token
from err import DisabledTokenException, ReadyTokenCheckerException
from exchange import PermissionRequest, TokenValidationRequest, TokenValidationService, TransactionRequest
from transit import TokenCarrier
from util import IdFactory, LoggingLevelRouter


class ReadyTokenChecker:
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks if a Token can be used in an activity.

    Attributes:
        validation_service: TokenValidationService
        
    Provides:
        -   def execute(self, request: ReadyRequest) -> ReadyDecision

    Super Class:
    """
    
    _validation_service: TokenValidationService
    
    def __init__(
            self,
            validation_service: Optional[TokenValidationService] | None = None,
    ):
        """
        Args:
            validation_service: Optional[TokenValidationService]
        """
        self._validation_service = validation_service
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            candidate: Token,
            permission_request: PermissionRequest,
            transaction_request: TransactionRequest,
    ) -> Decision:
        """
        Confirm a Token is in the ready state before use.

        Action:
            1.  Send an exception chain in the denial if either
                    -   The candidate is not a valid token
                    -   The token is not in an actionable state.
            2.  Otherwise, send the Decision approval.
        Args:
            candidate: Token
            permission_request: PermissionRequest
            transaction_request: TransactionRequest
        Result:
            Decision
        Raises:
            ReadyTokenCheckerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate gets flagged.
        validation = self._validation_service.extract_model(
            request=TokenValidationRequest(
                item=TokenCarrier(model=candidate),
                id=IdFactory.next_id("ValidationRequest"),
            )
        )
        if validation.is_failure:
            # Send the exception chain in the denial.
            return Decision.denial(
                exception=ReadyTokenCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ReadyTokenCheckerException.MSG,
                    err_code=ReadyTokenCheckerException_CODE,
                    ex=validation.exception,
                )
            )
        # --- Cast the validation payload for the readiness check. ---#
        item = cast(Token, validation.payload)
        token = item
        
        # Access readiness method if item is a KingToken.
        if isinstance(item, KingToken):
            token = cast(KingToken, item)
        # Access readiness method if the item is a CombatantToken.
        if isinstance(item, CombatantToken):
            token = cast(CombatantToken, item)
        # Handle the case that the token is disabled
        if token.is_not_ready:
            # Send the exception chain in the denial.
            return Decision.denial(
                exception=ReadyTokenCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ReadyTokenCheckerException.MSG,
                    err_code=ReadyTokenCheckerException_CODE,
                    ex=DisabledTokenException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=DisabledTokenException.MSG,
                        err_code=DisabledTokenException.ERR_CODE,
                    )
                )
            )
        # Otherwise, approve the token for use.
        return Decision.grant(
            transaction_request=transaction_request,
            permission_request=permission_request,
        )
        
        
            
        validation = self.validation_service.extract_model(
            request=TokenValidationRequest(
                item=TokenCarrier(model=candidate),
                id=IdFactory.next_id(class_name="TokenValidationRequest")
            )
        )
        if validation.is_failure:
            return Decision.denial(
                request=request,
                exception=ReadyTokenCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ReadyTokenCheckerException.MSG,
                    err_code=ReadyTokenCheckerException_CODE,
                    ex=validation.exception,
                )
            )
        token = cast(Token, validation.payload)
        applicant = token
        
        if isinstance(token, KingToken):
            applicant = cast(KingToken, token)
        if isinstance(token, CombatantToken):
            applicant = cast(CombatantToken, token)
            
        if applicant.is_not_ready:
            return Decision.denial(
                request=request,
                exception=ReadyTokenCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ReadyTokenCheckerException.MSG,
                    err_code=ReadyTokenCheckerException_CODE,
                    ex=DisabledTokenException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=DisabledTokenException.MSG,
                        err_code=DisabledTokenException.ERR_CODE,
                    )
                )
            )
        approval = PermissionRequest(
            id=request.id,
            authorization_applicant=applicant,
            activity=request.activity,
        )
        return Decision.grant(approval)