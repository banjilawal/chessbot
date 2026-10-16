# src/fabrication/builder/model/game/builder.py

"""
Module: fabrication.builder.model.game.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Game, GameBlueprint
from err import GameBuilderException
from exchange import GameBuildRequest
from fabrication import ModelBuilder, GameBuildLoader
from util import IdFactory, LoggingLevelRouter


class GameBuilder(ModelBuilder[Game]):
    """
    Role
        - Builder

    Responsibilities:
        1.  Create a Game from a blueprint.

    Attributes:
       loader: GameBuildLoader

    Provides:
        -   def execute(blueprint: GameBlueprint) -> BuildResult[Game]

    Super Class:
        ModelBuilder
    """
    
    def __init__(
            self,
            loader: Optional[GameBuildLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[GameBuildLoader]
        """
        super().__init__(loader=loader or GameBuildLoader())
    
    @property
    def loader(self) -> GameBuildLoader:
        return cast(GameBuildLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: GameBuildRequest) -> BuildResult[Game]:
        """
        Assemble a Game from the Blueprint's contents.
        Action:
            1.  Send an exception chain in the BuildResult if the loader does not produce
                a blueprint.
            2.  Otherwise, use the blueprint to assemble a Game for the success result.
        Args:
            request: GameBuildRequest
        Returns:
            BuildResult[Game]
        Raises:
            GameBuilderException
        """
        method = f"{self.__class__.__name__}"
        
        # --- Handoff the request to loader for blueprint prepartion. ---#
        result = self.loader.execute(request=request)
        # Handle the case that the loader aborts.
        if result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                GameBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=GameBuilderException.MSG,
                    err_code=GameBuilderException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Cast result payload for the product assembly. ---#
        blueprint = cast(GameBlueprint, result.payload)
        id = blueprint.id or IdFactory.next_id(class_name="Game")
        
        # --- Send the work product. ---#
        product = Game(
            id=id,
            arena=blueprint.arena,
            binder=blueprint.binder,
        )
        return BuildResult.success(product)