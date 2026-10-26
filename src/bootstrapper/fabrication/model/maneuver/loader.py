# src/bootstrap/fabrication/model/maneuver/loader.py

"""
Module: bootstrap.fabrication.model.maneuver.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Maneuver, ManeuverBlueprint
from err import ManeuverBuildLoaderException, ManeuverBuildRequestNullException
from exchange import ManeuverBuildRequest, ManeuverValidationRequest, ManeuverValidationService
from fabrication import ModelBuildLoader
from util import IdFactory, LoggingLevelRouter


class ManeuverBuildLoader(ModelBuildLoader[Maneuver]):
    """
    Role
        -   Authorization
        -   Bootstrapper
        
    Responsibilities:
        1.  Initialize the Maneuver build process by preparing a ManeuverBlueprint
            if the BuildRequest is correct.

    Attributes:
        validator: ManeuverValidationServer

    Provides:
        -   def execute(request: ManeuverBuildRequest) -> BuildResult[ManeuverBlueprint]

    Super Class:
        BuildLoader
    """
    
    def __init__(
            self,
            validator: Optional[ManeuverValidationService] | None = None,
    ):
        """
        Args:
            validator: Optional[ManeuverValidationServer]
        """
        super().__init__(validator=validator or ManeuverValidationService())
    
    @property
    def validator(self) -> ManeuverValidationService:
        return cast(ManeuverValidationService, super().validator)
        
    @LoggingLevelRouter.monitor
    def execute(self, request: ManeuverBuildRequest) -> BuildResult[ManeuverBlueprint]:
        """
        Prepare a ManeuverBlueprint which guarantees a safe Maneuver.
        
        Action:
            1.  Send an exception chain in the BuildResult if any of the following occur
                    -   The request is null or the wrong type.
                    -   The request does not contain a valid ManeuverBlueprint.
            2.  Otherwise, forward the safe blueprint.
        Args:
            request: ManeuverBuildRequest
        Returns:
            BuildResult[ManeuverBlueprint]
        Raises:
            ManeuverBuildLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Verify the request is safe. ---#
        priming = self.priming_validator.execute(
            candidate=request,
            target_model=ManeuverBuildRequest,
            null_exception=ManeuverBuildRequestNullException(),
        )
        # Handle the case that the request is flagged.
        if priming.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                ManeuverBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverBuildLoaderException.MSG,
                    err_code=ManeuverBuildLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast the priming result for additional processing. ---#
        build_request = cast(ManeuverBuildRequest, priming.payload)
        
        # Handle the case that the blueprint is faulty.
        blueprint_validation = self.validator.extract_blueprint(
            request=ManeuverValidationRequest(
                item=build_request.item,
                id=IdFactory.next_id(class_name="ManeuverValidationRequest")
            )
        )
        # Send the exception chain on failure.
        if blueprint_validation.is_failure:
            return BuildResult.failure(
                ManeuverBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverBuildLoaderException.MSG,
                    err_code=ManeuverBuildLoaderException.ERR_CODE,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product. ---#
        blueprint = cast(ManeuverBlueprint, blueprint_validation.payload)
        return BuildResult.success(blueprint)