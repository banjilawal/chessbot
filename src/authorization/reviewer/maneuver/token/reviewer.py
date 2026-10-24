# src/authorization/reviewer/maneuver/token/reviewer.py

"""
Module: authorization.reviewer.maneuver.token.reviewer
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import List, Optional, cast

from artifcat import ManeuverDecision
from authorization import (
    ActorChainable, ManeuverApplicantReviewer, ManeuverTokenDestinationChecker,
    ManeuverTokenOriginChecker, ReadyTokenChecker
)
from domain import Token
from err import ManeuverTokenReviewerException
from exchange import ManeuverAuthorizationRequest
from util import LoggingLevelRouter


class ManeuverTokenReviewer(ManeuverApplicantReviewer[Token]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Check if a Token can move.

    Attributes:
        ready_checker: ReadyTokenChecker
        origin_checker: ApplicantOriginChecker
        destination_checker: ApplicantDestinationChecker

    Provides:
        -   def execute(request: ManeuverAuthorizationRequest) -> ManeuverDecision

    Super Class:
        ManeuverApplicantReviewer
    """

    _origin_checker: ManeuverTokenOriginChecker
    _destination_checker: ManeuverTokenDestinationChecker

    
    def __init__(
            self,
            ready_checker: Optional[ReadyTokenChecker] | None = None,
            origin_checker: Optional[ManeuverTokenOriginChecker] | None = None,
            destination_checker: Optional[ManeuverTokenDestinationChecker] | None = None,
    ):
        """
        Args:
            ready_checker: Optional[ReadyTokenChecker]
            origin_checker: Optional[ApplicantOriginChecker]
            destination_checker: Optional[ApplicantDestinationChecker]
        """
        super().__init__(ready_checker=ready_checker or ReadyTokenChecker())
        self._origin_checker = origin_checker or ManeuverTokenOriginChecker()
        self._destination_checker = destination_checker or ManeuverTokenDestinationChecker()
        
    @property
    def ready_checker(self) -> ReadyTokenChecker:
        return cast(ReadyTokenChecker, super().ready_checker)
    
    @property
    def checkers(self) -> List[ActorChainable]:
        return [
            self._ready_checker,
            self._origin_checker,
            self._destination_checker,
        ]
    
    @LoggingLevelRouter.monitor
    def execute(self, request: ManeuverAuthorizationRequest) -> ManeuverDecision:
        """
        Decide if a Token can move.

        Action:
            1.  Send an exception chain in the Decision if any checker
                fails.
            2.  Otherwise, issue an approval.
        Args:
            request: ManeuverAuthorizationRequest
        Returns:
            ManeuverDecision
        Raises:
            ManeuverTokenReviewerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that ready_checker does not grant permission.
        decision = self._ready_checker.execute(request)
        # Send the exception chain in the denial.
        if decision.is_denial:
            return ManeuverDecision.denial(
                request=request,
                exception=ManeuverTokenReviewerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverTokenReviewerException.MSG,
                    err_code=ManeuverTokenReviewerException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # Handle the case that origin_checker does not grant permission.
        approved_request = decision.request
        decision = self._origin_checker.execute(approved_request)
        # Send the exception chain in the denial.
        if decision.is_denial:
            return ManeuverDecision.denial(
                request=request,
                exception=ManeuverTokenReviewerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverTokenReviewerException.MSG,
                    err_code=ManeuverTokenReviewerException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # Handle the case that destination_checker does not grant permission.
        approved_request = decision.request
        decision = self._destination_checker.execute(approved_request)
        if decision.is_denial:
            # Send the exception chain in the denial.
            return ManeuverDecision.denial(
                request=request,
                exception=ManeuverTokenReviewerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverTokenReviewerException.MSG,
                    err_code=ManeuverTokenReviewerException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # --- Prepare an approval of the actor. ---#
        approved_request = decision.request
        approval = ManeuverAuthorizationRequest(
            id=approved_request.id,
            activity=approved_request.activity,
            applicant=approved_request.applicant,
        )
        # --- Forward the approval. ---#
        return ManeuverDecision.grant(approval)
        