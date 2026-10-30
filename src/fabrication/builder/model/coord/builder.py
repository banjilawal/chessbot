# src/fabrication/builder/model/coord/builder.py

"""
Module: fabrication.builder.model.coord.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Coord, CoordBlueprint
from err import CoordBuilderException
from exchange import CoordBuildRequest
from fabrication import ModelBuilder, CoordBuildLoader
from util import LoggingLevelRouter


class CoordBuilder(ModelBuilder[Coord]):
    """
    Role
        - Builder

    Responsibilities:
        1.  Create a Coord from a blueprint.

    Attributes:
       loader: CoordBuildLoader

    Provides:
        -   def execute(blueprint: CoordBlueprint) -> BuildResult[Coord]

    Super Class:
        ModelBuilder
    """
    
    def __init__(
            self,
            loader: Optional[CoordBuildLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[CoordBuildLoader]
        """
        super().__init__(loader=loader or CoordBuildLoader())
    
    @property
    def loader(self) -> CoordBuildLoader:
        return cast(CoordBuildLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: CoordBuildRequest) -> BuildResult[Coord]:
        """
        Assemble a Coord from the Blueprint's contents.
        Action:
            1.  Send an exception chain in the BuildResult if the loader does not produce
                a blueprint.
            2.  Otherwise, use the blueprint to assemble a Coord for the success loading.
        Args:
            request: CoordBuildRequest
        Returns:
            BuildResult[Coord]
        Raises:
            CoordBuilderException
        """
        method = f"{self.__class__.__name__}"
        
        # --- Handoff the request to loader for blueprint prepartion. ---#
        bootstrap = self.loader.execute(request=request)
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                CoordBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=CoordBuilderException.MSG,
                    err_code=CoordBuilderException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Cast result payload for the product assembly. ---#
        blueprint = cast(CoordBlueprint, bootstrap.authorization_applicant)
        
        # --- Send the work product. ---#
        product = Coord(
            row=blueprint.row,
            column=blueprint.column,
            board=blueprint.board,
        )
        return BuildResult.success(product)