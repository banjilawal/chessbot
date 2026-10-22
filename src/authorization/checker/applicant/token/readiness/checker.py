# src/authorization/checker/applicant/token/readiness/checker.py

"""
Module: authorization.checker.applicant.token.readiness.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import Decision
from authorization import ApplicantChecker
from domain import CombatantToken, KingToken, Token
from err import DisabledTokenException, TokenNullException
from exchange import AuthorizationRequest
from util import LoggingLevelRouter


class ApplicantReadinessChecker(TokenApplicantChecker):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks that an applicant satisfies one of the Readiness requirements.

    Attributes:
        
    Provides:
        -   def execute(self, request: ReadinessRequest) -> ReadinessDecision

    Super Class:
        ApplicantChecker
    """
    
    @LoggingLevelRouter.monitor
    def execute(self, request: AuthorizationRequest) -> Decision:
        method = f"{self.__class__.__name__}.execute"
        
        applicant = None
        
        if isinstance(request.applicant, KingToken):
            applicant = cast(KingToken, request.applicant)
        if isinstance(request.applicant, CombatantToken):
            applicant = cast(CombatantToken, request.applicant)
        
        if applicant is None:
            return Decision.denial(
                request=request,
                exception=TokenNullException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenNullException.MSG,
                    err_code=TokenNullException.ERR_CODE,
                ),
            )
        if applicant.is_not_ready:
            return Decision.denial(
                request=request,
                exception=DisabledTokenException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=DisabledTokenException.MSG,
                    err_code=DisabledTokenException.ERR_CODE,
                )
            )
        approval = AuthorizationRequest(
            id=request.id,
            activity=request.activity,
            applicant=applicant,
        )
        return Decision.grant(approval)