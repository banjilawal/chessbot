# src/authorization/chain/model/token/__init__.py

"""
Module: authorization.chain.model.token.__init__
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import Decision
from authorization import ReadyChecker
from domain import CombatantToken, KingToken, Token
from err import DisabledTokenException
from exchange import AuthorizationRequest, TokenValidationRequest
from transit import TokenCarrier
from util import IdFactory, LoggingLevelRouter


class ReadyTokenChecker(ReadyChecker):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks that an applicant satisfies one of the Ready requirements.

    Attributes:
        
    Provides:
        -   def execute(self, request: ReadyRequest) -> ReadyDecision

    Super Class:
        ModelChecker
    """
    
    @LoggingLevelRouter.monitor
    def execute(self, request: AuthorizationRequest) -> Decision:
        method = f"{self.__class__.__name__}.execute"
        
        candidate = None
        
        if isinstance(request.applicant, KingToken):
            candidate = cast(KingToken, request.applicant)
        if isinstance(request.applicant, CombatantToken):
            candidate = cast(CombatantToken, request.applicant)
            
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
        approval = AuthorizationRequest(
            id=request.id,
            applicant=applicant,
            activity=request.activity,
        )
        return Decision.grant(approval)