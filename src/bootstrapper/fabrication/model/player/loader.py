# src/bootstrap/fabrication/model/player/loader.py

"""
Module: bootstrap.fabrication.model.player.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Player, PlayerBlueprint
from err import PlayerBuildLoaderException, PlayerBuildRequestNullException
from exchange import PlayerBuildRequest, PlayerValidationRequest, PlayerValidationService
from fabrication import ModelBuildLoader
from util import IdFactory, LoggingLevelRouter


class PlayerBuildLoader(ModelBuildLoader[Player]):
    """
    Role
        -   Authorization
        -   Bootstrapper
        
    Responsibilities:
        1.  Initialize the Player build process by preparing a PlayerBlueprint
            if the BuildRequest is correct.

    Attributes:
        validator: PlayerValidationServer

    Provides:
        -   def execute(request: PlayerBuildRequest) -> BuildResult[PlayerBlueprint]

    Super Class:
        BuildLoader
    """
    
    def __init__(
            self,
            validator: Optional[PlayerValidationService] | None = None,
    ):
        """
        Args:
            validator: Optional[PlayerValidationServer]
        """
        super().__init__(validator=validator or PlayerValidationService())
    
    @property
    def validator(self) -> PlayerValidationService:
        return cast(PlayerValidationService, super().validator)
        
    @LoggingLevelRouter.monitor
    def execute(self, request: PlayerBuildRequest) -> BuildResult[PlayerBlueprint]:
        """
        Prepare a PlayerBlueprint which guarantees a safe Player.
        
        Action:
            1.  Send an exception chain in the BuildResult if any of the following occur
                    -   The request is null or the wrong type.
                    -   The request does not contain a valid PlayerBlueprint.
            2.  Otherwise, forward the safe blueprint.
        Args:
            request: PlayerBuildRequest
        Returns:
            BuildResult[PlayerBlueprint]
        Raises:
            PlayerBuildLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Verify the request is safe. ---#
        priming = self.priming_validator.execute(
            candidate=request,
            target_model=PlayerBuildRequest,
            null_exception=PlayerBuildRequestNullException(),
        )
        # Handle the case that the request is flagged.
        if priming.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                PlayerBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerBuildLoaderException.MSG,
                    err_code=PlayerBuildLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast the priming result for additional processing. ---#
        build_request = cast(PlayerBuildRequest, priming.payload)
        
        # Handle the case that the blueprint is faulty.
        blueprint_validation = self.validator.extract_blueprint(
            request=PlayerValidationRequest(
                item=build_request.item,
                id=IdFactory.next_id(class_name="PlayerValidationRequest")
            )
        )
        # Send the exception chain on failure.
        if blueprint_validation.is_failure:
            return BuildResult.failure(
                PlayerBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PlayerBuildLoaderException.MSG,
                    err_code=PlayerBuildLoaderException.ERR_CODE,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product. ---#
        blueprint = cast(PlayerBlueprint, blueprint_validation.payload)
        return BuildResult.success(blueprint)