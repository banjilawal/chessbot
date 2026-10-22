# src/authorization/applicant/token/combatant/checker.py

"""
Module: authorization.applicant.token.combatant.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from artifcat import Decision, PromotionDecision
from authorization import Checker
from err import DisabledTokenException
from exchange import AuthorizationRequest, PromotionRequest
from util import LoggingLevelRouter


class CombatantReadinessChecker(Checker[PromotionRequest]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks if a Token can be promoted.

    Attributes:

    Provides:
        -   def request: PromotionRequest) -> PromotionDecision

    Super Class:
        Checker
    """
    

    @LoggingLevelRouter.monitor
    def execute(self, request: AuthorizationRequest) -> Decision:
        """
        Deny the request if requestor has already been promoted. Otherwise,
        forward an approval.
        
        Args:
            request: PromotionRequest
        Returns:
           PromotionDecision
        Raises:
            DisabledTokenException
        """
        method = f"{self.__class__.__name__}.execute"

        if request.applicant.is_not_ready:
            # Send an exception chain in the denial.
            return Decision.denial(
                request=request,
                exception=DisabledTokenException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=DisabledTokenException.MSG,
                    err_code=DisabledTokenException.ERR_CODE,
                ),
            )
        return PromotionDecision.grant(request)

        