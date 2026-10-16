# src/fabrication/builder/model/maneuver/builder.py

"""
Module: fabrication.builder.model.maneuver.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Maneuver, ManeuverBlueprint
from err import ManeuverBuilderException
from exchange import ManeuverBuildRequest
from fabrication import ModelBuilder, ManeuverBuildLoader
from util import LoggingLevelRouter


class ManeuverBuilder(ModelBuilder[Maneuver]):
    """
    Role
        - Builder

    Responsibilities:
        1.  Create a Maneuver from a blueprint.

    Attributes:
       loader: ManeuverBuildLoader

    Provides:
        -   def execute(blueprint: ManeuverBlueprint) -> BuildResult[Maneuver]

    Super Class:
        ModelBuilder
    """
    
    def __init__(
            self,
            loader: Optional[ManeuverBuildLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[ManeuverBuildLoader]
        """
        super().__init__(loader=loader or ManeuverBuildLoader())
    
    @property
    def loader(self) -> ManeuverBuildLoader:
        return cast(ManeuverBuildLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: ManeuverBuildRequest) -> BuildResult[Maneuver]:
        """
        Assemble a Maneuver from the Blueprint's contents.
        Action:
            1.  Send an exception chain in the BuildResult if the loader does not produce
                a blueprint.
            2.  Otherwise, use the blueprint to assemble a Maneuver for the success result.
        Args:
            request: ManeuverBuildRequest
        Returns:
            BuildResult[Maneuver]
        Raises:
            ManeuverBuilderException
        """
        method = f"{self.__class__.__name__}"
        
        # --- Handoff the request to loader for blueprint prepartion. ---#
        result = self.loader.execute(request=request)
        # Handle the case that the loader aborts.
        if result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                ManeuverBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverBuilderException.MSG,
                    err_code=ManeuverBuilderException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Cast result payload for the product assembly. ---#
        blueprint = cast(ManeuverBlueprint, result.payload)
        
        # --- Send the work product. ---#
        product = Maneuver(
            x=blueprint.x,
            y=blueprint.y,
        )
        return BuildResult.success(product)