# src/authorization/chain/role/attack/maneuver/checker.py

"""
Module: authorization.chain.role.attack.maneuver.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from artifcat import AttackDecision
from authorization import AttackRoleChecker
from domain import Attackable, Maneuver
from err import AuthorizationException, ManeuverConsistencyException
from exchange import AttackRequest, ManeuverValidationRequest
from transit import ManeuverCarrier
from util import IdFactory, LoggingLevelRouter


class AttackManeuverChecker(AttackRoleChecker[Attackable]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Grant permission to a Maneuver for an AttackRequest.

    Attributes:

    Provides:
        -   execute(request: AttackRequest) -> AttackDecision

    Super Class:
        AttackRoleChecker
    """
    
    def __init__(self):
        """"""
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(self, request: AttackRequest) -> AttackDecision:
        """
        Decide if an Attack can be made using a Maneuver.

        Action:
            1.  Deny permission to the Attack if any of the following occur
                    -   The activity is not a safe Maneuver.
                    -   The maneuver has an inconsistency.
                    -   There is no enemy at maneuver.destination.
            2.  Otherwise, issue a grant decision.
        Args:
            request: AttackRequest
        Returns:
           AttackDecision
        Raises:
          AttackManeuverCheckerException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that request.activity is not a safe maneuver.
        validation = self.validation_service.extract_model(
            request=ManeuverValidationRequest(
                item=ManeuverCarrier(model=request.activity_to_maneuver),
                id=IdFactory.next_id(class_name="ManeuverValidationRequest")
            )
        )
        if validation.is_failure:
            # Send the exception chain in the denial.
            return AttackDecision.denial(
                request=request,
                exception=AuthorizationException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AuthorizationException.MSG,
                    err_code=AuthorizationException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # Handle the case that the requested maneuver has an inconsistency.
        maneuver = cast(Maneuver, validation.payload)
        if maneuver.is_not_consistent:
            # Send the exception chain in the denial.
            return AttackDecision.denial(
                request=request,
                exception=AuthorizationException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AuthorizationException.MSG,
                    err_code=AuthorizationException.ERR_CODE,
                    ex=ManeuverConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=ManeuverConsistencyException.MSG,
                        err_code=ManeuverConsistencyException.ERR_CODE
                    ),
                )
            )
        # Handle the case that the requested maneuver does not have an enemy.
        if not maneuver.is_attacking_enemy:
            # Send the exception chain in the denial.
            return AttackDecision.denial(
                request=request,
                exception=AuthorizationException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AuthorizationException.MSG,
                    err_code=AuthorizationException.ERR_CODE,
                    ex=NullAttackVictimException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=NullAttackVictimException.MSG,
                        err_code=NullAttackVictimException.ERR_CODE
                    ),
                )
            )
        # --- Prepare an approval of the activity. ---#
        activity = cast(Attackable, maneuver)
        approval = AttackRequest(
            id=request.id,
            activity=activity,
            applicant=request.applicant,
        )
        # --- Forward the approval. ---#
        return AttackDecision.grant(approval)
 