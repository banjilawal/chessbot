# src/authorization/checker/role/attack/maneuver/checker.py

"""
Module: authorization.checker.role.attack.maneuver.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Optional, cast

from artifcat import AttackDecision
from authorization import AttackRoleChecker
from domain import Attack, Attackable, Maneuver
from err import AuthorizationException, ManeuverConsistencyException
from exchange import AttackRequest, ManeuverValidationRequest, ManeuverValidationService
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
        validation_service: ManeuverValidationService

    Provides:
        -   def execute(request: AttackRequest) -> AttackDecision

    Super Class:
        AttackRoleChecker
    """
    
    def __init__(
            self,
            validation_service: Optional[ManeuverValidationService] | None = None,
    ):
        """
        Args:
            validation_service: Optional[ManeuverValidationService]
        """
        super().__init__(
            validation_service=validation_service or ManeuverValidationService()
        )
        
    @property
    def validation_service(self) -> ManeuverValidationService:
        return cast(ManeuverValidationService, super().validation_service)
    
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
 