# src/fabrication/builder/model/vector/builder.py

"""
Module: fabrication.builder.model.vector.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Vector, VectorBlueprint
from err import VectorBuilderException
from exchange import VectorBuildRequest
from fabrication import ModelBuilder, VectorBuildLoader
from util import LoggingLevelRouter


class VectorBuilder(ModelBuilder[Vector]):
    """
    Role
        - Builder

    Responsibilities:
        1.  Create a Vector from a blueprint.

    Attributes:
       loader: VectorBuildLoader

    Provides:
        -   def execute(blueprint: VectorBlueprint) -> BuildResult[Vector]

    Super Class:
        ModelBuilder
    """
    
    def __init__(
            self,
            loader: Optional[VectorBuildLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[VectorBuildLoader]
        """
        super().__init__(loader=loader or VectorBuildLoader())
    
    @property
    def loader(self) -> VectorBuildLoader:
        return cast(VectorBuildLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: VectorBuildRequest) -> BuildResult[Vector]:
        """
        Assemble a Vector from the Blueprint's contents.
        Action:
            1.  Send an exception chain in the BuildResult if the loader does not produce
                a blueprint.
            2.  Otherwise, use the blueprint to assemble a Vector for the success loading.
        Args:
            request: VectorBuildRequest
        Returns:
            BuildResult[Vector]
        Raises:
            VectorBuilderException
        """
        method = f"{self.__class__.__name__}"
        
        # --- Handoff the request to loader for blueprint prepartion. ---#
        bootstrap = self.loader.execute(request=request)
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                VectorBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorBuilderException.MSG,
                    err_code=VectorBuilderException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Cast result payload for the product assembly. ---#
        blueprint = cast(VectorBlueprint, bootstrap.authorization_applicant)
        
        # --- Send the work product. ---#
        product = Vector(
            x=blueprint.x,
            y=blueprint.y,
        )
        return BuildResult.success(product)