# src/authorization/checker/role/maneuver/path/checker.py

"""
Module: authorization.checker.role.maneuver.path.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Optional, cast

from artifcat import ManeuverDecision
from authorization import ManeuverRoleChecker
from domain import Maneuver, Maneuverable, Path
from err import AuthorizationException
from exchange import ManeuverRequest, PathValidationRequest, PathValidationService
from transit import PathCarrier
from util import IdFactory, LoggingLevelRouter


class ManeuverPathChecker(ManeuverRoleChecker[Maneuverable]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Verifies a Maneuver meets minimum safety requirements before it
            can be approved for an activity.

    Attributes:
        validation_service: PathValidationService

    Provides:
        -   def execute(request: ManeuverRequest) -> ManeuverDecision

    Super Class:
        ManeuverRoleChecker
    """
    
    def __init__(
            self,
            validation_service: Optional[PathValidationService] | None = None,
    ):
        """
        Args:
            validation_service: Optional[PathValidationService]
        """
        super().__init__(
            validation_service=validation_service or PathValidationService()
        )
        
    @property
    def validation_service(self) -> PathValidationService:
        return cast(PathValidationService, super().validation_service)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: ManeuverRequest) -> ManeuverDecision:
        """
        Checks if a Maneuver meets the requirements to perform an activity.

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
            request=PathValidationRequest(
                item=PathCarrier(model=request.activity_to_path),
                id=IdFactory.next_id(class_name="PathValidationRequest")
            )
        )
        if validation.is_failure:
            # Send the exception chain on failure.
            return ManeuverDecision.denial(
                request=request,
                exception=AuthorizationException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AuthorizationException.MSG,
                    err_code=AuthorizationException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        path = cast(Path, validation.payload)
        approval = ManeuverRequest(
            id=request.id,
            activity=path,
            applicant=request.applicant,
        )
        # --- Forward the work product. ---#
        return ManeuverDecision.grant(approval)
 