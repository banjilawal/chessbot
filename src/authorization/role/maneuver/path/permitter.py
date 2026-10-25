# src/authorization/role/maneuver/path/checker.py

"""
Module: authorization.role.maneuver.path.checker
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ManeuverDecision
from authorization import ManeuverRolePermitter
from domain import Maneuverable, Path
from err import ManeuverPathPermitterException, PathConsistencyException
from exchange import ManeuverPermissionRequest, PathValidationRequest, PathValidationService
from transit import PathCarrier
from util import IdFactory, LoggingLevelRouter


class ManeuverPathPermitter(ManeuverRolePermitter[Maneuverable]):
    """
    Role:
        -   Authorization

    Responsibilities:
        1.  Grant permission to a Path for a ManeuverPermissionRequest.

    Attributes:
        validation_service: PathValidationService

    Provides:
        -   def execute(request: request: ManeuverPermissionRequest) -> ManeuverDecision

    Super Class:
        ManeuverRoleChecker
    """
    
    def __init__(self, validation_service: Optional[PathValidationService] | None = None):
        """
        Args:
            validation_service: Optional[PathValidationService]
        """
        super().__init__(validation_service=validation_service or PathValidationService())
    
    @property
    def validation_service(self) -> PathValidationService:
        return cast(PathValidationService, super().validation_service)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: ManeuverPermissionRequest) -> ManeuverDecision:
        """
        Decide if a Maneuver can be made on a Path.

        Action:
            1.  Deny permission to the Maneuver if any of the following occur
                    -   The activity is not a safe path.
                    -   The path has an inconsistency.
            2.  Otherwise, issue a grant decision.
        Args:
            request: ManeuverPermissionRequest
        Returns:
           ManeuverDecision
        Raises:
            ManeuverPathPermitterException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that request.activity is not a safe path.
        validation = self.validation_service.extract_model(
            request=PathValidationRequest(
                item=PathCarrier(model=request.activity_to_path),
                id=IdFactory.next_id(class_name="PathValidationRequest")
            )
        )
        if validation.is_failure:
            # Send the exception chain in the denial.
            return ManeuverDecision.denial(
                request=request,
                exception=ManeuverPathPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverPathPermitterException.MSG,
                    err_code=ManeuverPathPermitterException.ERR_CODE,
                    ex=validation.exception,
                )
            )
        # Handle the case that the requested path has an inconsistency.
        path = cast(Path, validation.payload)
        if path.not_consistent:
            # Send the exception chain in the denial.
            return ManeuverDecision.denial(
                request=request,
                exception=ManeuverPathPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverPathPermitterException.MSG,
                    err_code=ManeuverPathPermitterException.ERR_CODE,
                    ex=PathConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg=PathConsistencyException.MSG,
                        err_code=PathConsistencyException.ERR_CODE,
                    ),
                )
            )
        # --- Prepare an approval of the activity. ---#
        activity = cast(Maneuverable, path)
        approval = ManeuverPermissionRequest(
            id=request.id,
            activity=activity,
            applicant=request.applicant,
        )
        # --- Forward the approval. ---#
        return ManeuverDecision.grant(approval)