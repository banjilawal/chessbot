# src/fabrication/builder/model/square/builder.py

"""
Module: fabrication.builder.model.square.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Square, SquareBlueprint
from err import SquareBuilderException
from exchange import SquareBuildRequest
from fabrication import BuildFactory, SquareBuildLoader
from transit import SquareBuildRouter
from util import LoggingLevelRouter


class SquareBuilder(BuildFactory[Square]):
    """
    Role
        - Builder

    Responsibilities:
        1.  Create different Square products from the different types of blueprints.

    Attributes:
       loader: SquareBuildLoader
       router: SquareBuildRouter

    Provides:
        -   def execute(blueprint: SquareBlueprint) -> BuildResult[Square]

    Super Class:
        BuildFactory
    """
    
    def __init__(
            self,
            loader: Optional[SquareBuildLoader] | None = None,
            router: Optional[SquareBuildRouter] | None = None,
    ):
        """
        Args:
            loader: Optional[SquareBuildLoader]
            router: Optional[SquareBuildRouter]
        """
        super().__init__(
            loader=loader or SquareBuildLoader(),
            router=router or SquareBuildRouter(),
        )
    
    @property
    def loader(self) -> SquareBuildLoader:
        return cast(SquareBuildLoader, super().loader)
    
    @property
    def router(self) -> SquareBuildRouter:
        return cast(SquareBuildRouter, super().router)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: SquareBuildRequest) -> BuildResult[Square]:
        """
        Assemble a Square from the Blueprint's contents.
        Action:
            1.  Send an exception chain in the BuildResult if either:
                -   the loader does not produce a blueprint.
                -   the router does not return a product from the blueprint.
            2.  Otherwise, cast the product as a Square then send in the success result.
        Args:
            request: SquareBuildRequest
        Returns:
            BuildResult[Square]
        Raises:
            SquareBuilderException
        """
        method = f"{self.__class__.__name__}"
        
       # Handle the case that loader does not bootstrap the process.
        bootstrap = self.loader.execute(request=request)
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                SquareBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareBuilderException.MSG,
                    err_code=SquareBuilderException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Cast result payload for the product assembly. ---#
        blueprint = cast(SquareBlueprint, bootstrap.payload)
        result = self.router.execute(blueprint)
        
        # Handle the case that a product is not routed back.
        if result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                SquareBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareBuilderException.MSG,
                    err_code=SquareBuilderException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Send the work product. ---#
        return BuildResult.success(cast(Square, result.payload))