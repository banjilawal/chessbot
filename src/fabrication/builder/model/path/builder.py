# src/fabrication/builder/model/path/builder.py

"""
Module: fabrication.builder.model.path.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Path, PathBlueprint
from err import PathBuilderException
from exchange import PathBuildRequest
from fabrication import ModelBuilder, PathBuildLoader
from util import LoggingLevelRouter


class PathBuilder(ModelBuilder[Path]):
    """
    Role
        - Builder

    Responsibilities:
        1.  Create a Path from a blueprint.

    Attributes:
       loader: PathBuildLoader

    Provides:
        -   def execute(blueprint: PathBlueprint) -> BuildResult[Path]

    Super Class:
        ModelBuilder
    """
    
    def __init__(
            self,
            loader: Optional[PathBuildLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[PathBuildLoader]
        """
        super().__init__(loader=loader or PathBuildLoader())
    
    @property
    def loader(self) -> PathBuildLoader:
        return cast(PathBuildLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: PathBuildRequest) -> BuildResult[Path]:
        """
        Assemble a Path from the Blueprint's contents.
        Action:
            1.  Send an exception chain in the BuildResult if the loader does not produce
                a blueprint.
            2.  Otherwise, use the blueprint to assemble a Path for the success result.
        Args:
            request: PathBuildRequest
        Returns:
            BuildResult[Path]
        Raises:
            PathBuilderException
        """
        method = f"{self.__class__.__name__}"
        
        # --- Handoff the request to loader for blueprint prepartion. ---#
        result = self.loader.execute(request=request)
        # Handle the case that the loader aborts.
        if result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                PathBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=PathBuilderException.MSG,
                    err_code=PathBuilderException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Cast result payload for the product assembly. ---#
        blueprint = cast(PathBlueprint, result.payload)
        
        # --- Send the work product. ---#
        product = Path(
            x=blueprint.x,
            y=blueprint.y,
        )
        return BuildResult.success(product)