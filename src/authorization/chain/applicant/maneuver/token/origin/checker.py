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
        Decide if a Token can be move.

        Action:
            1.  Deny a maneuver if any of the following occur.
                    -   There is an inconsistency in the originating square.
                    -   The token is not at the origin.
            2.  Otherwise, issue an approval.
        Args:
            request: ManeuverRequest
        Returns:
           ManeuverDecision
        Raises:
            ManeuverTokenOriginCheckerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the path's origin has an inconsistency.  
        applicant = request.applicant
        origin = request.activity_to_path.origin
        if origin.is_not_consistent:
            # Send the exception chain in the denial.
            return ManeuverDecision.denial(
                request=request,
                exception=ManeuverTokenOriginCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverTokenOriginCheckerException.MSG,
                    err_code=ManeuverTokenOriginCheckerException.ERR_CODE,
                    ex=SquareConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=SquareConsistencyException.MSG,
                        err_code=SquareConsistencyException.ERR_CODE,
                    )
                )
            )
        # Handle the case that the applicant is not at the origin Square.
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