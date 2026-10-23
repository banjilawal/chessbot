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
from exchange import ManeuverRequest
from util import LoggingLevelRouter

class ApplicantDestinationChecker(ManeuverTokenChecker):
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
 