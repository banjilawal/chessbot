# src/authorization/checker/maneuver/destination/checker.py

"""
Module: authorization.checker.maneuver.destination.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from artifcat import ManeuverDecision
from authorization import ManeuverPathChecker
from domain import Path, Token
from err import BlockedDestinationException
from exchange import ManeuverPermissionRequest, ManeuverRequest
from util import LoggingLevelRouter


class ManeuverTokenDestinationChecker(ManeuverPathChecker):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Check that a Token and destination satisfy the ManeuverTransaction requirements.

    Attributes:

    Provides:
        -   def execute(
                    role: Path,
                    principal: Token,
                    transaction_request: ManeuverRequest,
                    permission_request: ManeuverPermissionRequest,
            ) -> ManeuverDecision

    Super Class:
        ManeuverPathChecker
    """
    
    @LoggingLevelRouter.monitor
    def execute(
            self,
            role: Path,
            principal: Token,
            transaction_request: ManeuverRequest,
            permission_request: ManeuverPermissionRequest,
    ) -> ManeuverDecision:
        """
        Checks if the token is not already at the maneuver endpoint.

        Action:
            1.  Send an exception in the denial if the token is either at path.destination,
                or the destination is occupied by a friend.
            2.  Otherwise, send a maneuver approval.
        Args:
            role: Path
            principal: Token
            transaction_request: ManeuverRequest
            permission_request: ManeuverPermissionRequest
        Returns:
           ManeuverDecision
        Raises:
            ManeuverTokenDestinationCheckerException
        """
        method = f"{self.__class__.__name__}.execute"
        destination = role.destination
        
        # Handle the case that the token is already at the destination
        if (
                destination.occupant == principal or
                destination.coord == principal.footstep.position
        ):
            # Send the exception chain in the denial.
            return ManeuverDecision.denial(
                exception=ManeuverTokenDestinationCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverTokenDestinationCheckerException.MSG,
                    err_code=ManeuverTokenDestinationCheckerException.ERR_CODE,
                    ex=PrematureArrivalExceptionException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PrematureArrivalExceptionException.MSG,
                        err_code=PrematureArrivalExceptionException.ERR_CODE,
                    ),
                )
            )
        # Handle the case that the destination is occupied by a friend.
        destination_occupant = destination.occupant
        if (
            destination_occupant is not None and
            principal.is_friend(destination_occupant)
        ):
            # Send an exception chain in the denial.
            return ManeuverDecision.denial(
                exception=ManeuverTokenDestinationCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverTokenDestinationCheckerException.MSG,
                    err_code=ManeuverTokenDestinationCheckerException.ERR_CODE,
                    ex=BlockedDestinationException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=BlockedDestinationException.MSG,
                        err_code=BlockedDestinationException.ERR_CODE,
                    ),
                )
            )
        # Otherwise send an approval.
        return ManeuverDecision.grant(
            transaction_request=transaction_request,
            permission_request=permission_request,
        )
        
        
        
        
        
