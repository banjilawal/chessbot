# src/authorization/checker/maneuver/destination/checker.py

"""
Module: authorization.checker.maneuver.destination.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import AttackDecision, ManeuverDecision
from authorization import ManeuverPathChecker
from domain import Path, Token
from err import BlockedDestinationException, ManeuverTokenDestinationCheckerException, PrematureArrivalException
from exchange import AttackPermissionRequest, AttackRequest, ManeuverPermissionRequest, ManeuverRequest
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
                    ex=PrematureArrivalException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PrematureArrivalException.MSG,
                        err_code=PrematureArrivalException.ERR_CODE,
                    ),
                )
            )
        # --- Extract the destination occupant for additional processing. ---#
        destination_occupant = destination.occupant
        
        # Handle the case that the destination is empty.
        if destination_occupant is None:
            # Send an approval.
            return ManeuverDecision.grant(
                transaction_request=transaction_request,
                permission_request=permission_request,
            )
        # Handle the case that the destination is occupied by an enemy.
        if principal.is_enemy(destination_occupant):
            # Send an attack approval.
            attack_request =  cast(AttackRequest, transaction_request)
            attack_permission = cast(AttackPermissionRequest, permission_request)
            return AttackDecision.grant(
                transaction_request=attack_request,
                permission_request=attack_permission,
            )
        # Otherwise the destination is occupied by a friend.
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
                )
            )
        )

        
        
        
        
        
