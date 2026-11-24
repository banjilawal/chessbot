# src/bootstrap/fabrication/model/encounter/loader.py

"""
Module: bootstrap.fabrication.model.encounter.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Encounter, EncounterBlueprint
from err import EncounterBuildLoaderException, EncounterBuildRequestNullException
from exchange import EncounterBuildRequest, EncounterValidationRequest, EncounterValidationService
from fabrication import ModelBuildLoader
from util import IdFactory, LoggingLevelRouter


class EncounterBuildLoader(ModelBuildLoader[Encounter]):
    """
    Role
        -   Authorization
        -   Bootstrap
        
    Responsibilities:
        1.  Initialize the Encounter build process by preparing a EncounterBlueprint
            if the BuildRequest is correct.

    Attributes:
        validator: EncounterValidationServer

    Provides:
        -   def execute(request: EncounterBuildRequest) -> BuildResult[EncounterBlueprint]

    Super Class:
        BuildLoader
    """
    
    def __init__(
            self,
            validator: Optional[EncounterValidationService] | None = None,
    ):
        """
        Args:
            validator: Optional[EncounterValidationServer]
        """
        super().__init__(validator=validator or EncounterValidationService())
    
    @property
    def validator(self) -> EncounterValidationService:
        return cast(EncounterValidationService, super().validator)
        
    @LoggingLevelRouter.monitor
    def execute(self, request: EncounterBuildRequest) -> BuildResult[EncounterBlueprint]:
        """
        Prepare a EncounterBlueprint which guarantees a safe Encounter.
        
        Action:
            1.  Send an exception chain in the BuildResult if any of the following occur
                    -   The request is null or the wrong type.
                    -   The request does not contain a valid EncounterBlueprint.
            2.  Otherwise, forward the safe blueprint.
        Args:
            request: EncounterBuildRequest
        Returns:
            BuildResult[EncounterBlueprint]
        Raises:
            EncounterBuildLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Verify the request is safe. ---#
        priming = self.priming_validator.execute(
            candidate=request,
            target_model=EncounterBuildRequest,
            null_exception=EncounterBuildRequestNullException(),
        )
        # Handle the case that the request is flagged.
        if priming.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                EncounterBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterBuildLoaderException.MSG,
                    err_code=EncounterBuildLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast the priming result for additional processing. ---#
        build_request = cast(EncounterBuildRequest, priming.authorization_applicant)
        
        # Handle the case that the blueprint is faulty.
        blueprint_validation = self.validator.extract_blueprint(
            request=EncounterValidationRequest(
                item=build_request.item,
                id=IdFactory.next_id(class_name="EncounterValidationRequest")
            )
        )
        # Send the exception chain on failure.
        if blueprint_validation.is_failure:
            return BuildResult.failure(
                EncounterBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterBuildLoaderException.MSG,
                    err_code=EncounterBuildLoaderException.ERR_CODE,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product. ---#
        blueprint = cast(EncounterBlueprint, blueprint_validation.payload)
        return BuildResult.success(blueprint)