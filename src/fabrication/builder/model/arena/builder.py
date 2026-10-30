# src/fabrication/builder/model/arena/builder.py

"""
Module: fabrication.builder.model.arena.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Arena, ArenaBlueprint
from err import ArenaBuilderException, ArenaConsistencyException
from exchange import ArenaBuildRequest
from fabrication import ModelBuilder, ArenaBuildLoader
from util import IdFactory, LoggingLevelRouter


class ArenaBuilder(ModelBuilder[Arena]):
    """
    Role
        - Builder

    Responsibilities:
        1.  Create a Arena from a blueprint.

    Attributes:
       loader: ArenaBuildLoader

    Provides:
        -   def execute(blueprint: ArenaBlueprint) -> BuildResult[Arena]

    Super Class:
        ModelBuilder
    """
    
    def __init__(
            self,
            loader: Optional[ArenaBuildLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[ArenaBuildLoader]
        """
        super().__init__(loader=loader or ArenaBuildLoader())
    
    @property
    def loader(self) -> ArenaBuildLoader:
        return cast(ArenaBuildLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: ArenaBuildRequest) -> BuildResult[Arena]:
        """
        Assemble a Arena from the Blueprint's contents.
        Action:
            1.  Send an exception chain in the BuildResult if the loader does not produce
                a blueprint.
            2.  Otherwise, use the blueprint to assemble a Arena for the success loading.
        Args:
            request: ArenaBuildRequest
        Returns:
            BuildResult[Arena]
        Raises:
            ArenaBuilderException
        """
        method = f"{self.__class__.__name__}"
        
        # --- Handoff the request to loader for blueprint prepartion. ---#
        bootstrap = self.loader.execute(request=request)
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                ArenaBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaBuilderException.MSG,
                    err_code=ArenaBuilderException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Cast result payload for the product assembly. ---#
        blueprint = cast(ArenaBlueprint, bootstrap.authorization_applicant)
        id = blueprint.id or IdFactory.next_id(class_name="Arena")
        
        # --- Send the work product. ---#
        product = Arena(
            id=id,
            game=blueprint.game,
            board=blueprint.board,
            binder=blueprint.binder,
        )
        if product.game != blueprint.game.arena:
            # Send the exception chain on failure.
            return BuildResult.failure(
                ArenaBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ArenaBuilderException.MSG,
                    err_code=ArenaBuilderException.ERR_CODE,
                    ex=ArenaConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg="Game is already assigned to a different Arena instance.",
                        err_code="ARENA_GAME_CONSISTENCY_ERROR"
                    ),
                )
            )
        return BuildResult.success(product)