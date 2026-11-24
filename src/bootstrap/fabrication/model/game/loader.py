# src/bootstrap/fabrication/model/game/loader.py

"""
Module: bootstrap.fabrication.model.game.loader
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Game, GameBlueprint
from err import GameBuildLoaderException, GameBuildRequestNullException
from exchange import GameBuildRequest, GameValidationRequest, GameValidationService
from fabrication import ModelBuildLoader
from util import IdFactory, LoggingLevelRouter


class GameBuildLoader(ModelBuildLoader[Game]):
    """
    Role
        -   Authorization
        -   Bootstrap
        
    Responsibilities:
        1.  Initialize the Game build process by preparing a GameBlueprint
            if the BuildRequest is correct.

    Attributes:
        validator: GameValidationServer

    Provides:
        -   def execute(request: GameBuildRequest) -> BuildResult[GameBlueprint]

    Super Class:
        BuildLoader
    """
    
    def __init__(
            self,
            validator: Optional[GameValidationService] | None = None,
    ):
        """
        Args:
            validator: Optional[GameValidationServer]
        """
        super().__init__(validator=validator or GameValidationService())
    
    @property
    def validator(self) -> GameValidationService:
        return cast(GameValidationService, super().validator)
        
    @LoggingLevelRouter.monitor
    def execute(self, request: GameBuildRequest) -> BuildResult[GameBlueprint]:
        """
        Prepare a GameBlueprint which guarantees a safe Game.
        
        Action:
            1.  Send an exception chain in the BuildResult if any of the following occur
                    -   The request is null or the wrong type.
                    -   The request does not contain a valid GameBlueprint.
            2.  Otherwise, forward the safe blueprint.
        Args:
            request: GameBuildRequest
        Returns:
            BuildResult[GameBlueprint]
        Raises:
            GameBuildLoaderException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Verify the request is safe. ---#
        priming = self.priming_validator.execute(
            candidate=request,
            target_model=GameBuildRequest,
            null_exception=GameBuildRequestNullException(),
        )
        # Handle the case that the request is flagged.
        if priming.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                GameBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameBuildLoaderException.MSG,
                    err_code=GameBuildLoaderException.ERR_CODE,
                    ex=priming.exception,
                )
            )
        # --- Cast the priming result for additional processing. ---#
        build_request = cast(GameBuildRequest, priming.authorization_applicant)
        
        # Handle the case that the blueprint is faulty.
        blueprint_validation = self.validator.extract_blueprint(
            request=GameValidationRequest(
                item=build_request.item,
                id=IdFactory.next_id(class_name="GameValidationRequest")
            )
        )
        # Send the exception chain on failure.
        if blueprint_validation.is_failure:
            return BuildResult.failure(
                GameBuildLoaderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameBuildLoaderException.MSG,
                    err_code=GameBuildLoaderException.ERR_CODE,
                    ex=blueprint_validation.exception
                )
            )
        # --- Forward the work product. ---#
        blueprint = cast(GameBlueprint, blueprint_validation.payload)
        return BuildResult.success(blueprint)