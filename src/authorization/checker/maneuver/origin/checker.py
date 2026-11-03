# src/authorization/checker/maneuver/origin/checker.py

"""
Module: authorization.checker.maneuver.origin.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from artifcat import ManeuverDecision
from authorization import ManeuverPathChecker
from domain import Path, SquareState, Token
from exchange import ManeuverPermissionRequest, ManeuverRequest
from util import LoggingLevelRouter


class ManeuverTokenOriginChecker(ManeuverPathChecker):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Check that a Token and Path satisfy the ManeuverTransaction requirements.

    Attributes:

    Provides:
        -   def execute(
                    role: Path,
                    principal: Token,
                    transaction_request: ManeuverRequest,
                    permission_request: ManeuverPermissionRequest,
            ) -> ManeuverDecision

    Super Class:
        RoleChecker
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
        Checks if the token is at the correct starting point.

        Action:
            1.  Send an exception in the denial if the token is not
                at path.origin.
            2.  Otherwise, send a maneuver approval.
        Args:
            role: Path
            principal: Token
            transaction_request: ManeuverRequest
            permission_request: ManeuverPermissionRequest
        Returns:
           ManeuverDecision
        Raises:
            ManeuverTokenOriginCheckerException
        """
        method = f"{self.__class__.__name__}.execute"
        origin = role.origin
        
        # Handle the case that the token is not at the origin.
        if (
                origin.occupant != principal and
                origin.coord != principal.footstep.position and
                origin.state != SquareState.OCCUPIED
        ):
            # Send the exception chain in the denial.
            return ManeuverDecision.denial(
                exception=ManeuverTokenOriginCheckerException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverTokenOriginCheckerException.MSG,
                    err_code=ManeuverTokenOriginCheckerException.ERR_CODE,
                    ex=TokenPathOriginConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=TokenPathOriginConsistencyException.MSG,
                        err_code=TokenPathOriginConsistencyException.ERR_CODE,
                    ),
                )
            )
        # Otherwise send an approval.
        return ManeuverDecision.grant(
            transaction_request=transaction_request,
            permission_request=permission_request,
        )
        
        
        
        
        
