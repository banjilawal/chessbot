# src/fabrication/builder/model/board/builder.py

"""
Module: fabrication.builder.model.board.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Board, BoardBlueprint
from err import BoardBuilderException, BoardConsistencyException
from exchange import BoardBuildRequest
from fabrication import ModelBuilder, BoardBuildLoader
from util import IdFactory, LoggingLevelRouter


class BoardBuilder(ModelBuilder[Board]):
    """
    Role
        - Builder

    Responsibilities:
        1.  Create a Board from a blueprint.

    Attributes:
       loader: BoardBuildLoader

    Provides:
        -   def execute(blueprint: BoardBlueprint) -> BuildResult[Board]

    Super Class:
        ModelBuilder
    """
    
    def __init__(
            self,
            loader: Optional[BoardBuildLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[BoardBuildLoader]
        """
        super().__init__(loader=loader or BoardBuildLoader())
    
    @property
    def loader(self) -> BoardBuildLoader:
        return cast(BoardBuildLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: BoardBuildRequest) -> BuildResult[Board]:
        """
        Assemble a Board from the Blueprint's contents.
        Action:
            1.  Send an exception chain in the BuildResult if the loader does not produce
                a blueprint.
            2.  Otherwise, use the blueprint to assemble a Board for the success loading.
        Args:
            request: BoardBuildRequest
        Returns:
            BuildResult[Board]
        Raises:
            BoardBuilderException
        """
        method = f"{self.__class__.__name__}"
        
        # --- Handoff the request to loader for blueprint prepartion. ---#
        bootstrap = self.loader.execute(request=request)
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                BoardBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardBuilderException.MSG,
                    err_code=BoardBuilderException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Cast result payload for the product assembly. ---#
        blueprint = cast(BoardBlueprint, bootstrap.authorization_applicant)
        id = blueprint.id or IdFactory.next_id(class_name="Board")
        
        # --- Send the work product. ---#
        product = Board(
            id=id,
            arena=blueprint.arena,
            binder=blueprint.binder,
        )
        if product not in blueprint.arena.binder.to_list:
            # Send the exception chain on failure.
            return BuildResult.failure(
                BoardBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=BoardBuilderException.MSG,
                    err_code=BoardBuilderException.ERR_CODE,
                    ex=BoardConsistencyException(
                        cls_mthd=method,
                        cls_name=self.__class__.__name__,
                        msg="Arena is already assigned to a different Board instance.",
                        err_code="BOARD_ARENA_CONSISTENCY_ERROR"
                    ),
                )
            )
        return BuildResult.success(product)