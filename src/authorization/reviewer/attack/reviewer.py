# src/authorization/reviewer/attack/reviewer.py

"""
Module: authorization.reviewer.attack.reviewer
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import List, Optional, Type, cast

from artifcat import AttackDecision
from authorization import ApplicantReviewer
from err import ApplicantApproverException
from exchange import AttackRequest

from util import LoggingLevelRouter


class AttackApplicantReviewer(ApplicantReviewer[AttackRequest]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Checks if an Actor satisfies the requirements to perform an
            activity.

    Attributes:
        valid_applicant_checker: ValidTokenChecker
        origin_checker: ApplicantOriginChecker
        readiness_checker: ApplicantReadinessChecker
        destination_checker: ApplicantDestinationChecker

    Provides:
        -   def execute(request: AttackRequest) -> AttackDecision

    Super Class:
        ApplicantReview
    """

    _pawn_checker: AttackPawnTokenChecker
    _origin_checker: ApplicantOriginChecker
    _readiness_checker: ApplicantReadinessChecker
    _destination_checker: ApplicantDestinationChecker

    
    def __init__(
            self,
            valid_applicant_checker: Optional[ValidTokenChecker] | None = None,
            pawn_checker: Optional[AttackPawnTokenChecker] | None = None,
            origin_checker: Optional[ApplicantOriginChecker] | None = None,
            readiness_checker: Optional[ApplicantReadinessChecker] | None = None,
            destination_checker: Optional[ApplicantDestinationChecker] | None = None,
    ):
        """
        Args:
            valid_applicant_checker: Optional[ValidTokenChecker]
            pawn_checker: Optional[AttackPawnTokenChecker]
            origin_checker: Optional[ApplicantOriginChecker]
            readiness_checker: Optional[ApplicantReadinessChecker]
            destination_checker: Optional[ApplicantDestinationChecker]
        """
        super().__init__(valid_applicant_checker=valid_applicant_checker or ValidTokenChecker())
        self._pawn_checker = pawn_checker or AttackPawnTokenChecker()
        self._readiness_checker = readiness_checker or ApplicantReadinessChecker()
        self._origin_checker = origin_checker or ApplicantOriginChecker()
        self._destination_checker = destination_checker or ApplicantDestinationChecker()
        
    @property
    def valid_applicant_checker(self) -> ValidTokenChecker:
        return cast(Type[ValidTokenChecker], super().valid_applicant_checker)
    
    @property
    def checkers(self) -> List[ApplicantChecker]:
        return [
            self._valid_applicant_checker,
            self._pawn_checker,
            self._readiness_checker,
            self._origin_checker,
            self._destination_checker,
        ]
    
    @LoggingLevelRouter.monitor
    def execute(self, request: AttackRequest) -> AttackDecision:
        method = f"{self.__class__.__name__}.execute"
        
        decision = self._valid_applicant_checker.execute(request)
        if decision.is_denial:
            return AttackDecision.denial(
                request=request,
                exception=ApplicantApproverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ApplicantApproverException.MSG,
                    err_code=ApplicantApproverException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        approved_request = decision.request
        decision = self._readiness_checker.execute(approved_request)
        if decision.is_denial:
            return AttackDecision.denial(
                request=request,
                exception=ApplicantApproverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ApplicantApproverException.MSG,
                    err_code=ApplicantApproverException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        approved_request = decision.request
        decision = self._origin_checker.execute(approved_request)
        if decision.is_denial:
            return AttackDecision.denial(
                request=request,
                exception=ApplicantApproverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ApplicantApproverException.MSG,
                    err_code=ApplicantApproverException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        approved_request = decision.request
        decision = self._destination_checker.execute(approved_request)
        if decision.is_denial:
            return AttackDecision.denial(
                request=request,
                exception=ApplicantApproverException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ApplicantApproverException.MSG,
                    err_code=ApplicantApproverException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        approved_request = decision.request
        approval = AttackRequest(
            id=approved_request.id,
            activity=approved_request.activity,
            applicant=approved_request.applicant,
        )
        return AttackDecision.grant(approval)
        