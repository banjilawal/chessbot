# src/fabrication/builder/model/rank/builder.py

"""
Module: fabrication.builder.model.rank.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Rank, RankBlueprint
from err import RankBuilderException
from exchange import RankBuildRequest
from fabrication import ModelBuilder, RankBuildLoader
from util import LoggingLevelRouter


class RankBuilder(ModelBuilder[Rank]):
    """
    Role
        - Builder

    Responsibilities:
        1.  Create a Rank from a blueprint.

    Attributes:
       loader: RankBuildLoader

    Provides:
        -   def execute(blueprint: RankBlueprint) -> BuildResult[Rank]

    Super Class:
        ModelBuilder
    """
    
    def __init__(
            self,
            loader: Optional[RankBuildLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[RankBuildLoader]
        """
        super().__init__(loader=loader or RankBuildLoader())
    
    @property
    def loader(self) -> RankBuildLoader:
        return cast(RankBuildLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: RankBuildRequest) -> BuildResult[Rank]:
        """
        Assemble a Rank from the Blueprint's contents.
        Action:
            1.  Send an exception chain in the BuildResult if the loader does not produce
                a blueprint.
            2.  Otherwise, use the blueprint to assemble a Rank for the success loading.
        Args:
            request: RankBuildRequest
        Returns:
            BuildResult[Rank]
        Raises:
            RankBuilderException
        """
        method = f"{self.__class__.__name__}"
        
        # --- Handoff the request to loader for blueprint prepartion. ---#
        loading = self.loader.execute(request=request)
        # Handle the case that the loader aborts.
        if loading.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                RankBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RankBuilderException.MSG,
                    err_code=RankBuilderException.ERR_CODE,
                    ex=loading.exception,
                )
            )
        # --- Cast result payload for the product assembly. ---#
        blueprint = cast(RankBlueprint, loading.payload)
        
        # --- Send the work product. ---#
        product = Rank(
            row=blueprint.row,
            column=blueprint.column,
            board=blueprint.board,
        )
        return BuildResult.success(product)