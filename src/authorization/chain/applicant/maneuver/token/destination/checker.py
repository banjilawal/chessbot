# src/authorization/chain/applicant/maneuver/tokendestination/checker.py

"""
Module: authorization.chain.applicant.maneuver.token.destination.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from artifcat import ManeuverDecision
from authorization import ManeuverTokenChecker
from domain import Maneuver
from exchange import ManeuverRequest
from util import LoggingLevelRouter

class ApplicantDestinationChecker(ManeuverTokenChecker):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Verifies a Maneuver applicant is on its enemy's rank destination.

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
            ApplicantDestinationCheckerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        applicant = request.applicant
        destination_occupant = request.activity_to_path.destination.occupant
        
        if destination_occupant == applicant:
            return ManeuverDecision.denial(
                request=request,
                exception=ApplicantDestinationCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ApplicantDestinationCheckerException.MSG,
                    err_code=ApplicantDestinationCheckerException.ERR_CODE,
                    ex=TravelerAtDestintionException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TravelerAtDestintionException.MSG,
                        err_code=TravelerAtDestintionException.ERR_CODE,
                    )
                )
            )
        if (
                destination_occupant is not None and
                applicant.is_friend(destination_occupant)
        ):
            return ManeuverDecision.denial(
                request=request,
                exception=ApplicantDestinationCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ApplicantDestinationCheckerException.MSG,
                    err_code=ApplicantDestinationCheckerException.ERR_CODE,
                    ex=BlockedDestintionException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=BlockedDestintionException.MSG,
                        err_code=BlockedDestintionException.ERR_CODE,
                    )
                )
            )
        # --- Forward the work product. ---
        approval = ManeuverRequest(
            id=request.id,
            applicant=request.applicant,
            activity=request.activity,
        )
        return ManeuverDecision.grant(approval)
 