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

class ManeuverTokenOriginChecker(ManeuverTokenChecker):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Check if a Token can move.

    Attributes:

    Provides:
        -   execute(request: ManeuverRequest) -> ManeuverDecision

    Super Class:
        ManeuverTokenChecker
    """
    
    @LoggingLevelRouter.monitor
    def execute(self, request: ManeuverRequest) -> ManeuverDecision:
        """
        Decide if a Token can move.

        Action:
            1.  Deny a ManeuverRequest if the token is not in the originating
                square.
            2.  Otherwise, issue an approval.
        Args:
            request: ManeuverRequest
        Returns:
           ManeuverDecision
        Raises:
            ManeuverTokenOriginCheckerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the applicant is not at the origin Square.
        applicant = request.applicant
        origin = request.activity_to_path.origin
        if (
                origin.occupant != applicant or
                origin.coord != applicant.footstep.position
        ):
            # Send the exception chain in the denial.
            return ManeuverDecision.denial(
                request=request,
                exception=ManeuverTokenOriginCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverTokenOriginCheckerException.MSG,
                    err_code=ManeuverTokenOriginCheckerException.ERR_CODE,
                    ex=TokenPositionException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenPositionException.MSG,
                        err_code=TokenPositionException.ERR_CODE,
                    )
                )
            )
        # --- Prepare an approval of the actor. ---#
        approval = ManeuverRequest(
            id=request.id,
            applicant=request.applicant,
            activity=request.activity,
        )
        # --- Forward the approval. ---#
        return ManeuverDecision.grant(approval)