# src/authorization/chain/applicant/maneuver/tokenorigin/checker.py

"""
Module: authorization.chain.applicant.maneuver.token.origin.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from artifcat import ManeuverDecision
from authorization import ManeuverTokenChecker
from exchange import ManeuverRequest
from util import LoggingLevelRouter

class ApplicantOriginChecker(ManeuverTokenChecker):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Verifies a Maneuver applicant is on its enemy's rank origin.

    Attributes:

    Provides:
        -   def execute(self, request: ManeuverRequest) -> ManeuverDecision

    Super Class:
        ManeuverTokenChecker
    """
    
    @LoggingLevelRouter.monitor
    def execute(self, request: ManeuverRequest) -> ManeuverDecision:
        """
        Checks if a Token meets the requirements to perform an activity.

        Args:
            request: request: ManeuverRequest
        Returns:
           ManeuverDecision
        Raises:
            ManeuverTokenChecker
        """
        method = f"{self.__class__.__name__}.execute"
        
        applicant = request.applicant
        origin = request.activity_to_path.origin
        if origin.is_not_consistent:
            return ManeuverDecision.denial(
                request=request,
                exception=ApplicantOriginCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ApplicantOriginCheckerException.MSG,
                    err_code=ApplicantOriginCheckerException.ERR_CODE,
                    ex=SquareConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareConsistencyException.MSG,
                        err_code=SquareConsistencyException.ERR_CODE,
                    )
                )
            )
        if (
                origin.occupant != applicant or
                origin.coord != applicant.footstep.position
        ):
            return ManeuverDecision.denial(
                request=request,
                exception=ApplicantOriginCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ApplicantOriginCheckerException.MSG,
                    err_code=ApplicantOriginCheckerException.ERR_CODE,
                )
            )
        # --- Forward the work product. ---
        approval = ManeuverRequest(
            id=request.id,
            applicant=request.applicant,
            activity=request.activity,
        )
        return ManeuverDecision.grant(approval)
 