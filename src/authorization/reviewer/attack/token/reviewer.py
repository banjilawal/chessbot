# src/authorization/reviewer/attack/token/reviewer.py

"""
Module: authorization.reviewer.attack.token.reviewer
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import List, Optional

from artifcat import AttackDecision
from authorization import (
    ActorChainable, DoubleAttackChecker, AttackApplicantReviewer, AttackPawnTokenChecker,
    AttackRowChecker, ReadyTokenChecker,
)
from domain import Token
from err import AttackTokenReviewerException
from exchange import AttackPermissionRequest
from util import LoggingLevelRouter


class AttackTokenReviewer(AttackApplicantReviewer[Token]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Check if a Token can be promoted.

    Attributes:
        ready_checker: ReadyTokenChecker
        pawn_checker: AttackPawnTokenChecker
        attack_row_checker: AttackRowChecker
        double_attack_checker: DoubleAttackChecker

    Provides:
        -   def execute(request: AttackPermissionRequest) -> AttackDecision

    Super Class:
        AttackApplicantReviewer
    """
    _ready_checker: ReadyTokenChecker
    _pawn_checker: AttackPawnTokenChecker
    _attack_row_checker: AttackRowChecker
    _double_attack_checker: DoubleAttackChecker
    
    def __init__(
            self,
            ready_checker: Optional[ReadyTokenChecker] | None = None,
            pawn_checker: Optional[AttackPawnTokenChecker] | None = None,
            attack_row_checker: Optional[AttackRowChecker] | None = None,         
            double_attack_checker: Optional[DoubleAttackChecker] | None = None,
    ):
        """
        Args:
            ready_checker: Optional[ReadyTokenChecker]
            pawn_checker: Optional[AttackPawnTokenChecker]
            attack_row_checker: Optional[AttackRowChecker]
            double_attack_checker: Optional[DoubleAttackChecker]
        """
        super().__init__(ready_checker=ready_checker or ReadyTokenChecker())
        self._pawn_checker = pawn_checker or AttackPawnTokenChecker()
        self._attack_row_checker = attack_row_checker or AttackRowChecker()
        self._double_attack_checker = double_attack_checker or DoubleAttackChecker()
    
    @property
    def checkers(self) -> List[ActorChainable]:
        return [
            self._ready_checker,
            self._pawn_checker,
            self._attack_row_checker,
            self._double_attack_checker,
        ]
    
    @LoggingLevelRouter.monitor
    def execute(self, request: AttackPermissionRequest) -> AttackDecision:
        """
        Decide if a Token can be promoted
        
        Action:
        Args:
            request: AttackPermissionRequest
        Returns:
            AttackDecision
        Raises:
            AttackTokenReviewerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the token is not ready.
        decision = self._ready_checker.execute(request)
        if decision.request_is_denied:
            # Send the exception chain in the denial.
            return AttackDecision.denial(
                request=request,
                exception=AttackTokenReviewerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackTokenReviewerException.MSG,
                    err_code=AttackTokenReviewerException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # Handle the pawn_checker does not grant permission.
        approved_request = decision.request
        decision = self._pawn_checker.execute(approved_request)
        if decision.request_is_denied:
            # Send the exception chain in the denial.
            return AttackDecision.denial(
                request=request,
                exception=AttackTokenReviewerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackTokenReviewerException.MSG,
                    err_code=AttackTokenReviewerException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # Handle the row_checker does not grant permission.
        approved_request = decision.request
        decision = self._attack_row_checker.execute(approved_request)
        if decision.request_is_denied:
            # Send the exception chain in the denial.
            return AttackDecision.denial(
                request=request,
                exception=AttackTokenReviewerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackTokenReviewerException.MSG,
                    err_code=AttackTokenReviewerException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # Handle the double_attack_checker does not grant permission.
        approved_request = decision.request
        decision = self._double_attack_checker.execute(approved_request)
        if decision.request_is_denied:
            # Send the exception chain in the denial.
            return AttackDecision.denial(
                request=request,
                exception=AttackTokenReviewerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackTokenReviewerException.MSG,
                    err_code=AttackTokenReviewerException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # --- Prepare an approval of the actor. ---#
        approved_request = decision.request
        approval = AttackPermissionRequest(
            id=approved_request.id,
            activity=approved_request.activity,
            authorization_applicant=approved_request.applicant,
        )
        # --- Forward the approval. ---#
        return AttackDecision.grant(approval)

        