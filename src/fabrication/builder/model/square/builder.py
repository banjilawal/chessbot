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
from fabrication import ModelBuilder, SquareBuildLoader
from util import LoggingLevelRouter


class SquareBuilder(ModelBuilder[Square]):
    """
    Role
        - Builder

    Responsibilities:
        1.  Create a Square from a blueprint.

    Attributes:
       loader: SquareBuildLoader

    Provides:
        -   def execute(blueprint: SquareBlueprint) -> BuildResult[Square]

    Super Class:
        ModelBuilder
    """
    
    def __init__(
            self,
            loader: Optional[SquareBuildLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[SquareBuildLoader]
        """
        super().__init__(loader=loader or SquareBuildLoader())
    
    @property
    def loader(self) -> SquareBuildLoader:
        return cast(SquareBuildLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: SquareBuildRequest) -> BuildResult[Square]:
        """
        Assemble a Square from the Blueprint's contents.
        Action:
            1.  Send an exception chain in the BuildResult if the loader does not produce
                a blueprint.
            2.  Otherwise, use the blueprint to assemble a Square for the success loading.
        Args:
            request: SquareBuildRequest
        Returns:
            BuildResult[Square]
        Raises:
            SquareBuilderException
        """
        method = f"{self.__class__.__name__}"
        
        # --- Handoff the request to loader for blueprint prepartion. ---#
        loading = self.loader.execute(request=request)
        # Handle the case that the loader aborts.
        if loading.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                SquareBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=SquareBuilderException.MSG,
                    err_code=SquareBuilderException.ERR_CODE,
                    ex=loading.exception,
                )
            )
        # --- Cast result payload for the product assembly. ---#
        blueprint = cast(SquareBlueprint, loading.payload)
        
        # --- Send the work product. ---#
        product = Square(
            x=blueprint.x,
            y=blueprint.y,
        )
        return BuildResult.success(product)