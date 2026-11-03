# src/authorization/chain/model/token/__init__.py

"""
Module: authorization.chain.model.token.__init__
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import Decision
from domain import CombatantToken, KingToken, Token
from err import DisabledTokenException
from exchange import PermissionRequest, TokenValidationRequest, TransactionRequest
from exchange.service.validation.model.token import TokenValidationService
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
    
    def __init__(self, validation_service: Optional[TokenValidationService] | None = None):
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
        method = f"{self.__class__.__name__}.execute"
        
        validation = self._validation_service.extract_model(
            request=TokenValidationRequest(
                item=TokenCarrier(model=candidate),
                id=IdFactory.next_id("ValidationRequest"),
            )
        )
        if validation.is_failure:
            return Decision.denial(
                exception=ReadyTokenCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ReadyTokenCheckerException.MSG,
                    err_code=ReadyTokenCheckerException_CODE,
                    ex=validation.exception,
                )
            )
        item = cast(Token, validation.payload)
        token = item
        
        if isinstance(item, KingToken):
            token = cast(KingToken, item)
        if isinstance(item, CombatantToken):
            token = cast(CombatantToken, item)
        if token.is_not_ready:
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