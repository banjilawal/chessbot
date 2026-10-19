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
from fabrication import BuildFactory, RankBuildLoader
from transit import RankBuildRouter
from util import LoggingLevelRouter


class RankBuilder(BuildFactory[Rank]):
    """
    Role
        - Builder

    Responsibilities:
        1.  Create different Rank products from the different types of blueprints.

    Attributes:
       loader: RankBuildLoader
       router: RankBuildRouter

    Provides:
        -   def execute(blueprint: RankBlueprint) -> BuildResult[Rank]

    Super Class:
        BuildFactory
    """
    
    def __init__(
            self,
            loader: Optional[RankBuildLoader] | None = None,
            router: Optional[RankBuildRouter] | None = None,
    ):
        """
        Args:
            loader: Optional[RankBuildLoader]
            router: Optional[RankBuildRouter]
        """
        super().__init__(
            loader=loader or RankBuildLoader(),
            router=router or RankBuildRouter(),
        )
    
    @property
    def loader(self) -> RankBuildLoader:
        return cast(RankBuildLoader, super().loader)
    
    @property
    def router(self) -> RankBuildRouter:
        return cast(RankBuildRouter, super().router)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: RankBuildRequest) -> BuildResult[Rank]:
        """
        Assemble a Rank from the Blueprint's contents.
        Action:
            1.  Send an exception chain in the BuildResult if either:
                -   the loader does not produce a blueprint.
                -   the router does not return a product from the blueprint.
            2.  Otherwise, cast the product as a Rank then send in the success result.
        Args:
            request: RankBuildRequest
        Returns:
            BuildResult[Rank]
        Raises:
            RankBuilderException
        """
        method = f"{self.__class__.__name__}"
        
        # --- Handoff the request to loader for blueprint preparation. ---#
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
        result = self.router.execute(blueprint)
        
        # Handle the case that a product is not routed back.
        if result.is_failure:
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
        # --- Send the work product. ---#
        return BuildResult.success(cast(Rank, result.payload))