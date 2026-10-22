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
        1.  Verifies a Attack meets minimum safety requirements before it
            can be approved for an activity.

    Attributes:

    Provides:
        -   def execute(request: AttackRequest) -> AttackDecision

    Super Class:
        AttackRoleChecker
    """
    
    def __init__(self):
        """"""
        super().__init__()
    
    @LoggingLevelRouter.monitor
    def execute(self, request: AttackRequest) -> AttackDecision:
        """
        Checks if a Attack meets the requirements to perform an activity.

        Args:
            request: AuthorizationRequest
        Returns:
           Decision
        Raises:
            AuthorizationException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the candidate gets flagged.
        validation = self.validation_service.extract_model(
            request=ManeuverValidationRequest(
                item=ManeuverCarrier(model=request.activity_to_maneuver),
                id=IdFactory.next_id(class_name="ManeuverValidationRequest")
            )
        )
        if validation.is_failure:
            # Send the exception chain on failure.
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
        maneuver = cast(Maneuver, validation.payload)
        if maneuver.is_not_consistent:
            # Send the exception chain on failure.
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
        if not maneuver.is_attacking_enemy:
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
        activity = cast(Attackable, maneuver)
        approval = AttackRequest(
            id=request.id,
            activity=activity,
            applicant=request.applicant,
        )
        # --- Forward the work product. ---#
        return AttackDecision.grant(approval)
 