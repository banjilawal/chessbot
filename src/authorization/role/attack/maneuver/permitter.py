# src/authorization/role/attack/maneuver/permitter.py

"""
Module: authorization.role.attack.maneuver.permitter
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AttackDecision
from authorization import AttackRolePermitter
from domain import Attackable, Maneuver
from err import AttackManeuverPermitterException, ManeuverConsistencyException, NullAttackVictimException
from exchange import AttackAuthorizationRequest, ManeuverValidationRequest, ManeuverValidationService
from transit import ManeuverCarrier
from util import IdFactory, LoggingLevelRouter


class AttackManeuverPermitter(AttackRolePermitter[Attackable]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Grant permission to a Maneuver for an AttackAuthorizationRequest.

    Attributes:
        validation_service: ManeuverValidationService

    Provides:
        -   execute(request: AttackAuthorizationRequest) -> AttackDecision

    Super Class:
        AttackRolePermitter
    """
    
    def __init__(self, validation_service: Optional[ManeuverValidationService] | None = None):
        """
        Args:
            validation_service: Optional[ManeuverValidationService]
        """
        super().__init__(validation_service=validation_service or ManeuverValidationService())
    
    @property
    def validation_service(self) -> ManeuverValidationService:
        return cast(ManeuverValidationService, super().validation_service)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: AttackAuthorizationRequest) -> AttackDecision:
        """
        Decide if an Attack can be made using a Maneuver.

        Action:
            1.  Deny permission to the Attack if any of the following occur
                    -   The activity is not a safe Maneuver.
                    -   The maneuver has an inconsistency.
                    -   There is no enemy at maneuver.destination.
            2.  Otherwise, issue a grant decision.
        Args:
            request: AttackAuthorizationRequest
        Returns:
           AttackDecision
        Raises:
          AttackManeuverPermitterException
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
                exception=AttackManeuverPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackManeuverPermitterException.MSG,
                    err_code=AttackManeuverPermitterException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # Handle the case that the requested maneuver has an inconsistency.
        maneuver = cast(Maneuver, validation.payload)
        if maneuver.is_not_consistent:
            # Send the exception chain in the denial.
            return AttackDecision.denial(
                request=request,
                exception=AttackManeuverPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackManeuverPermitterException.MSG,
                    err_code=AttackManeuverPermitterException.ERR_CODE,
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
                exception=AttackManeuverPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackManeuverPermitterException.MSG,
                    err_code=AttackManeuverPermitterException.ERR_CODE,
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
        approval = AttackAuthorizationRequest(
            id=request.id,
            activity=activity,
            applicant=request.applicant,
        )
        # --- Forward the approval. ---#
        return AttackDecision.grant(approval)
 