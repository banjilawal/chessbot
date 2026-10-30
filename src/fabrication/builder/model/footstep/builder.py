# src/fabrication/builder/model/footstep/builder.py

"""
Module: fabrication.builder.model.footstep.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Footstep, FootstepBlueprint
from err import FootstepBuilderException
from exchange import FootstepBuildRequest
from fabrication import ModelBuilder, FootstepBuildLoader
from util import LoggingLevelRouter


class FootstepBuilder(ModelBuilder[Footstep]):
    """
    Role
        - Builder

    Responsibilities:
        1.  Create a Footstep from a blueprint.

    Attributes:
       loader: FootstepBuildLoader

    Provides:
        -   def execute(blueprint: FootstepBlueprint) -> BuildResult[Footstep]

    Super Class:
        ModelBuilder
    """
    
    def __init__(
            self,
            loader: Optional[FootstepBuildLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[FootstepBuildLoader]
        """
        super().__init__(loader=loader or FootstepBuildLoader())
    
    @property
    def loader(self) -> FootstepBuildLoader:
        return cast(FootstepBuildLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: FootstepBuildRequest) -> BuildResult[Footstep]:
        """
        Assemble a Footstep from the Blueprint's contents.
        Action:
            1.  Send an exception chain in the BuildResult if the loader does not produce
                a blueprint.
            2.  Otherwise, use the blueprint to assemble a Footstep for the success loading.
        Args:
            request: FootstepBuildRequest
        Returns:
            BuildResult[Footstep]
        Raises:
            FootstepBuilderException
        """
        method = f"{self.__class__.__name__}"
        
        # --- Handoff the request to loader for blueprint prepartion. ---#
        bootstrap = self.loader.execute(request=request)
        if bootstrap.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                FootstepBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=FootstepBuilderException.MSG,
                    err_code=FootstepBuilderException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Cast result payload for the product assembly. ---#
        blueprint = cast(FootstepBlueprint, bootstrap.authorization_applicant)
        
        # --- Send the work product. ---#
        product = Footstep(
            position=blueprint.position,
            previous_position=blueprint.previous_position,
        )
        return BuildResult.success(product)