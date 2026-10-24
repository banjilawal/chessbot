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
from err import BlockedDestinationException, TravelerAtDestinationException
from exchange import ManeuverAuthorizationRequest
from util import LoggingLevelRouter

class ManeuverTokenDestinationChecker(ManeuverTokenChecker):
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
    def execute(self, request: ManeuverAuthorizationRequest) -> ManeuverDecision:
        """
        Decide if a Token can move.

        Action:
            1.  Deny a ManeuverAuthorizationRequest if any of the following occur
                    -   The token is already at the destination square.
                    -   The destination is occupied by a friend.
            2.  Otherwise, issue an approval.
        Args:
            request: ManeuverAuthorizationRequest
        Returns:
           ManeuverDecision
        Raises:
            ManeuverTokenDestinationCheckerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the applicant is already at the destination.
        applicant = request.applicant
        destination = request.activity_to_path.destination
        if (
                destination.occupant == applicant or
                destination.coord == applicant.footstep.position
        ):
            # Send the exception chain in the denial.
            return ManeuverDecision.denial(
                request=request,
                exception=TravelerAtDestinationException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TravelerAtDestinationException.MSG,
                    err_code=TravelerAtDestinationException.ERR_CODE,
                )
            )
        # Handle the case that the destination square is occupied by a friend.
        destination_occupant = destination.occupant
        if (
                destination_occupant is not None and
                applicant.is_friend(destination_occupant)
        ):
            # Send the exception chain in the denial.
            return ManeuverDecision.denial(
                request=request,
                exception=BlockedDestinationException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BlockedDestinationException.MSG,
                    err_code=BlockedDestinationException.ERR_CODE,
                )
            )
        # --- Prepare an approval of the actor. ---#
        approval = ManeuverAuthorizationRequest(
            id=request.id,
            applicant=request.applicant,
            activity=request.activity,
        )
        # --- Forward the approval. ---#
        return ManeuverDecision.grant(approval)