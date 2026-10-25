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
from err import ManeuverCandidateOriginException
from exchange import ManeuverPermissionRequest
from util import LoggingLevelRouter

class ManeuverTokenOriginChecker(ManeuverTokenChecker):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Check if a Token can move.

    Attributes:

    Provides:
        -   execute(request: ManeuverAuthorizationRequest) -> ManeuverDecision

    Super Class:
        ManeuverTokenChecker
    """
    
    @LoggingLevelRouter.monitor
    def execute(self, request: ManeuverPermissionRequest) -> ManeuverDecision:
        """
        Decide if a Token can move.

        Action:
            1.  Deny a ManeuverAuthorizationRequest if the token is not in the originating
                square.
            2.  Otherwise, issue an approval.
        Args:
            request: ManeuverAuthorizationRequest
        Returns:
           ManeuverDecision
        Raises:
            ManeuverCandidateOriginException
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
                exception=ManeuverCandidateOriginException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverCandidateOriginException.MSG,
                    err_code=ManeuverCandidateOriginException.ERR_CODE,
                )
            )
        # --- Prepare an approval of the actor. ---#
        approval = ManeuverPermissionRequest(
            id=request.id,
            applicant=request.applicant,
            activity=request.activity,
        )
        # --- Forward the approval. ---#
        return ManeuverDecision.grant(approval)