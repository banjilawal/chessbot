# src/bootstrap/fabrication/model/arena/loader.py

"""
Module: bootstrap.fabrication.model.arena.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Arena, ArenaBlueprint
from err import ArenaBuildLoaderException, ArenaBuildRequestNullException
from exchange import ArenaBuildRequest, ArenaValidationRequest, ArenaValidationService
from fabrication import ModelBuildLoader
from util import IdFactory, LoggingLevelRouter


class ArenaBuildLoader(ModelBuildLoader[Arena]):
    """
    Role
        -   Authorization
        -   Bootstrapper
        
    Responsibilities:
        1.  Initialize the Arena build process by preparing a ArenaBlueprint
            if the BuildRequest is correct.

    Attributes:
        validator: ArenaValidationServer

    Provides:
        -   def execute(request: ArenaBuildRequest) -> BuildResult[ArenaBlueprint]

    Super Class:
        BuildLoader
    """
    
    def __init__(
            self,
            validator: Optional[ArenaValidationService] | None = None,
    ):
        """
        Args:
            validator: Optional[ArenaValidationServer]
        """
        super().__init__(validator=validator or ArenaValidationService())
    
    @property
    def validator(self) -> ArenaValidationService:
        return cast(ArenaValidationService, super().validator)
        
    @LoggingLevelRouter.monitor
    def execute(self, request: ArenaBuildRequest) -> BuildResult[ArenaBlueprint]:
        """
        Prepare a ArenaBlueprint which guarantees a safe Arena.
        
        Action:
            1.  Send an exception chain in the BuildResult if any of the following occur
                    -   The request is null or the wrong type.
                    -   The request does not contain a valid ArenaBlueprint.
            2.  Otherwise, forward the safe blueprint.
        Args:
            request: ArenaBuildRequest
        Returns:
            BuildResult[ArenaBlueprint]
        Raises:
            ArenaBuildLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Verify the request is safe. ---#
        priming = self.priming_validator.execute(
            candidate=request,
            target_model=ArenaBuildRequest,
            null_exception=ArenaBuildRequestNullException(),
        )
        # Handle the case that the request is flagged.
        if priming.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                ArenaBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaBuildLoaderException.MSG,
                    err_code=ArenaBuildLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast the priming result for additional processing. ---#
        build_request = cast(ArenaBuildRequest, priming.payload)
        
        # Handle the case that the blueprint is faulty.
        blueprint_validation = self.validator.extract_blueprint(
            request=ArenaValidationRequest(
                item=build_request.item,
                id=IdFactory.next_id(class_name="ArenaValidationRequest")
            )
        )
        # Send the exception chain on failure.
        if blueprint_validation.is_failure:
            return BuildResult.failure(
                ArenaBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaBuildLoaderException.MSG,
                    err_code=ArenaBuildLoaderException.ERR_CODE,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product. ---#
        blueprint = cast(ArenaBlueprint, blueprint_validation.payload)
        return BuildResult.success(blueprint)