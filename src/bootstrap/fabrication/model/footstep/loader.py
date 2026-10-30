# src/bootstrap/fabrication/model/footstep/loader.py

"""
Module: bootstrap.fabrication.model.footstep.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Footstep, FootstepBlueprint
from err import FootstepBuildLoaderException, FootstepBuildRequestNullException
from exchange import FootstepBuildRequest, FootstepValidationRequest, FootstepValidationService
from fabrication import ModelBuildLoader
from util import IdFactory, LoggingLevelRouter


class FootstepBuildLoader(ModelBuildLoader[Footstep]):
    """
    Role
        -   Authorization
        -   Bootstrap
        
    Responsibilities:
        1.  Initialize the Footstep build process by preparing a FootstepBlueprint
            if the BuildRequest is correct.

    Attributes:
        validator: FootstepValidationServer

    Provides:
        -   def execute(request: FootstepBuildRequest) -> BuildResult[FootstepBlueprint]

    Super Class:
        BuildLoader
    """
    
    def __init__(
            self,
            validator: Optional[FootstepValidationService] | None = None,
    ):
        """
        Args:
            validator: Optional[FootstepValidationServer]
        """
        super().__init__(validator=validator or FootstepValidationService())
    
    @property
    def validator(self) -> FootstepValidationService:
        return cast(FootstepValidationService, super().validator)
        
    @LoggingLevelRouter.monitor
    def execute(self, request: FootstepBuildRequest) -> BuildResult[FootstepBlueprint]:
        """
        Prepare a FootstepBlueprint which guarantees a safe Footstep.
        
        Action:
            1.  Send an exception chain in the BuildResult if any of the following occur
                    -   The request is null or the wrong type.
                    -   The request does not contain a valid FootstepBlueprint.
            2.  Otherwise, forward the safe blueprint.
        Args:
            request: FootstepBuildRequest
        Returns:
            BuildResult[FootstepBlueprint]
        Raises:
            FootstepBuildLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Verify the request is safe. ---#
        priming = self.priming_validator.execute(
            candidate=request,
            target_model=FootstepBuildRequest,
            null_exception=FootstepBuildRequestNullException(),
        )
        # Handle the case that the request is flagged.
        if priming.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                FootstepBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=FootstepBuildLoaderException.MSG,
                    err_code=FootstepBuildLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast the priming result for additional processing. ---#
        build_request = cast(FootstepBuildRequest, priming.payload)
        
        # Handle the case that the blueprint is faulty.
        blueprint_validation = self.validator.extract_blueprint(
            request=FootstepValidationRequest(
                item=build_request.item,
                id=IdFactory.next_id(class_name="FootstepValidationRequest")
            )
        )
        # Send the exception chain on failure.
        if blueprint_validation.is_failure:
            return BuildResult.failure(
                FootstepBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=FootstepBuildLoaderException.MSG,
                    err_code=FootstepBuildLoaderException.ERR_CODE,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product. ---#
        blueprint = cast(FootstepBlueprint, blueprint_validation.payload)
        return BuildResult.success(blueprint)