# src/fabrication/builder/model/encounter/builder.py

"""
Module: fabrication.builder.model.encounter.builder
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import BuildResult
from domain import Encounter, EncounterBlueprint
from err import EncounterBuilderException
from exchange import EncounterBuildRequest
from fabrication import ModelBuilder, EncounterBuildLoader
from util import LoggingLevelRouter


class EncounterBuilder(ModelBuilder[Encounter]):
    """
    Role
        - Builder

    Responsibilities:
        1.  Create a Encounter from a blueprint.

    Attributes:
       loader: EncounterBuildLoader

    Provides:
        -   def execute(blueprint: EncounterBlueprint) -> BuildResult[Encounter]

    Super Class:
        ModelBuilder
    """
    
    def __init__(
            self,
            loader: Optional[EncounterBuildLoader] | None = None,
    ):
        """
        Args:
            loader: Optional[EncounterBuildLoader]
        """
        super().__init__(loader=loader or EncounterBuildLoader())
    
    @property
    def loader(self) -> EncounterBuildLoader:
        return cast(EncounterBuildLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: EncounterBuildRequest) -> BuildResult[Encounter]:
        """
        Assemble a Encounter from the Blueprint's contents.
        Action:
            1.  Send an exception chain in the BuildResult if the loader does not produce
                a blueprint.
            2.  Otherwise, use the blueprint to assemble a Encounter for the success result.
        Args:
            request: EncounterBuildRequest
        Returns:
            BuildResult[Encounter]
        Raises:
            EncounterBuilderException
        """
        method = f"{self.__class__.__name__}"
        
        # --- Handoff the request to loader for blueprint prepartion. ---#
        result = self.loader.execute(request=request)
        # Handle the case that the loader aborts.
        if result.is_failure:
            # Send the exception chain on failure.
            return BuildResult.failure(
                EncounterBuilderException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=EncounterBuilderException.MSG,
                    err_code=EncounterBuilderException.ERR_CODE,
                    ex=result.exception,
                )
            )
        # --- Cast result payload for the product assembly. ---#
        blueprint = cast(EncounterBlueprint, result.payload)
        
        # --- Send the work product. ---#
        product = Encounter(
            x=blueprint.x,
            y=blueprint.y,
        )
        return BuildResult.success(product)